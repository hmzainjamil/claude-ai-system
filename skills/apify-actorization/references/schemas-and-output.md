# Schemas and Output Configuration

## Input Schema

Map your application's inputs to `.actor/input_schema.json`. Validate against the JSON Schema from the `@apify/json_schemas` npm package (`input.schema.json`).

```json
{
    "title": "My Actor Input",
    "type": "object",
    "schemaVersion": 1,
    "properties": {
        "startUrl": {
            "title": "Start URL",
            "type": "string",
            "description": "The URL to start processing from",
            "editor": "textfie