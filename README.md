# NOW website

## Board data import/export

The Django admin supports import and export for these board-related models:

- `Role types`
- `Persons`
- `Board nodes`
- `Board assignments`

Use the admin import/export actions from the matching model pages.

### Export order

Export in this order to keep the related IDs easy to follow:

1. `Role types`
2. `Persons`
3. `Board nodes`
4. `Board assignments`

### Import order

Import in this order because later models depend on earlier ones:

1. `Role types`
2. `Persons`
3. `Board nodes`
4. `Board assignments`

### Important notes

- Keep the `id` column unchanged when moving data between environments. The board import files use IDs to reconnect foreign keys.
- `Board assignments` references `person`, `node`, and `role` by ID, so those records must exist before assignments are imported.
- `Board nodes` references `parent` by ID. Root nodes should have an empty `parent` value.
- If a `Board nodes` import file contains parent/child rows together, place parent rows before their children.
- If you are updating an existing site, import the full related set from the same export batch to avoid broken references.
