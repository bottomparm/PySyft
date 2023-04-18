# third party

# syft absolute
from syft.service.metadata.metadata_stash import MetadataStash
from syft.service.metadata.node_metadata import NodeMetadata
from syft.service.metadata.node_metadata import NodeMetadataUpdate


def add_mock_metadata(
    root_verify_key, metadata_stash: MetadataStash, metadata: NodeMetadata
) -> NodeMetadata:
    # prepare: add mock metadata
    result = metadata_stash.partition.set(root_verify_key, metadata)
    assert result.is_ok()

    created_metadata = result.ok()
    assert created_metadata is not None

    return created_metadata


def test_metadatastash_set(
    root_verify_key, metadata_stash: MetadataStash, metadata: NodeMetadata
) -> None:
    result = metadata_stash.set(root_verify_key, metadata)
    assert result.is_ok()

    created_metadata = result.ok()
    assert isinstance(created_metadata, NodeMetadata)
    assert created_metadata == metadata
    assert metadata.id in metadata_stash.partition.data


def test_metadatastash_update(
    root_verify_key,
    metadata_stash: MetadataStash,
    metadata: NodeMetadata,
    update_metadata: NodeMetadataUpdate,
) -> None:
    # prepare: add a mock metadata
    mock_metadata = add_mock_metadata(root_verify_key, metadata_stash, metadata)

    # update mock_metadata according to update_metadata
    update_kwargs = update_metadata.to_dict(exclude_none=True).items()
    for field_name, value in update_kwargs:
        setattr(mock_metadata, field_name, value)

    # update the metadata in the stash
    result = metadata_stash.update(root_verify_key, metadata=mock_metadata)

    assert result.is_ok()
    updated_metadata = result.ok()
    assert isinstance(updated_metadata, NodeMetadata)
    assert mock_metadata == updated_metadata