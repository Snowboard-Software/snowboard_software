# Templates: Automate Your Data Catalog Management

## Overview

Templates are a powerful feature that allows you to automatically apply consistent metadata, properties, tags, and data quality checks across multiple data assets in your catalog. Think of templates as "rules" that help you manage your data catalog at scale, ensuring consistency and saving valuable time.

### Why Use Templates?

- **Save Time**: Apply changes to hundreds of assets in seconds instead of editing each one manually
- **Ensure Consistency**: Maintain uniform metadata standards across your organization
- **Reduce Errors**: Eliminate manual mistakes by automating repetitive tasks
- **Improve Governance**: Enforce data quality standards systematically

## Getting Started

### Who Can Use Templates?

Templates are available to users with **Admin** roles. If you need access, please contact your system administrator.

### Accessing Templates

1. Navigate to the **Settings** page from the main menu
2. Scroll down to find the **Templates** section
3. Click on the Templates panel to expand it

## Creating Your First Template

### Step 1: Start Creating a Template

Click the **"Add Template"** button to open the template creation dialog.

### Step 2: Name Your Template

Choose a descriptive name that clearly indicates what this template does. For example:
- "Marketing Department Assets"
- "Production Tables Quality Checks"
- "Financial Data Ownership"

**Note**: Once created, template names cannot be changed, so choose carefully!

### Step 3: Define Your Pattern

The pattern (regex) determines which assets your template will affect. This uses a simple dot notation:

**Pattern Format**: `database.schema.table`

**Examples**:
- `PROD_DB.*` - Matches everything in the PROD_DB database
- `.*\.CUSTOMERS` - Matches all tables named CUSTOMERS in any schema
- `MARKETING_DB\..*\.FACT_.*` - Matches all tables starting with FACT_ in the MARKETING_DB database

### Step 4: Preview Affected Assets

After entering your pattern, click **"Evaluate Regex"** to see exactly what will be affected. The system will show you counts for:
- Databases
- Schemas
- Tables
- Columns
- Functions
- Tableau assets (sites, projects, workbooks, views, datasources)
- Terms
- Metrics

**Important**: Always review these numbers to ensure your pattern matches what you expect!

### Step 5: Configure Properties and Tags

#### Properties
Add any properties you want to apply to the matched assets:
- **Owner**: Assign responsibility to specific users
- **Description**: Add standardized descriptions
- **Custom Properties**: Any additional metadata fields your organization uses

#### Tags
Add tags to categorize and organize your assets. Tags are useful for:
- Marking data sensitivity levels
- Identifying departmental ownership
- Flagging assets for review
- Creating custom groupings

### Step 6: Enable Data Quality Checks

Select which automated checks should run on the matched assets:
- **Stable Volume**: Monitors for unexpected changes in data volume
- **Schema Change**: Detects structural changes to tables
- **Technical Freshness**: Tracks when data was last updated
- **Content Freshness**: Monitors data content changes
- **Data Redundancy**: Identifies duplicate data
- **Null Values**: Checks for unexpected null values
- **Accepted Categories**: Validates categorical data
- **Stable Measures**: Monitors key metrics for stability

### Step 7: Configure Additional Options

- **Approve assets**: Automatically publishes matched assets to make them visible to all users
- **Overwrite properties**: Replace existing properties instead of adding to them

### Step 8: Save and Apply

Click **"Save"** to create your template. The system will immediately apply it to all matching assets.

## Managing Existing Templates

### Viewing Templates

Your templates are displayed in a table showing:
- Template name
- Pattern (regex) used
- Edit and delete actions

### Editing Templates

1. Click the **edit icon** next to a template
2. Modify any settings except the name
3. Re-evaluate the regex if you've changed the pattern
4. Save your changes

### Deleting Templates

1. Click the **delete icon** next to a template
2. Confirm the deletion

**Note**: Deleting a template removes the template rule but does NOT remove properties or tags that were already applied to assets.

## Common Use Cases

### Use Case 1: Department-Wide Ownership

**Scenario**: Assign all marketing data to the marketing team

**Template Setup**:
- Name: "Marketing Data Ownership"
- Pattern: `MARKETING_DB.*`
- Properties: Owner = "marketing-team@company.com"
- Enable "Approve assets" to make them publicly visible

### Use Case 2: Production Data Quality

**Scenario**: Enable quality checks on all production tables

**Template Setup**:
- Name: "Production Quality Monitoring"
- Pattern: `PROD_.*\..*`
- Checks: Enable all relevant quality checks
- Tags: Add "production", "monitored"

### Use Case 3: Sensitive Data Flagging

**Scenario**: Mark all tables containing customer information

**Template Setup**:
- Name: "Customer Data Security"
- Pattern: `.*\.(CUSTOMER|CLIENT|USER).*`
- Tags: Add "PII", "sensitive", "restricted"
- Properties: Data Classification = "Confidential"

### Use Case 4: Development Environment Labeling

**Scenario**: Clearly mark all development databases

**Template Setup**:
- Name: "Development Environment"
- Pattern: `(DEV|TEST|STAGING)_.*`
- Tags: Add "non-production", "development"
- Properties: Environment = "Development"

## Best Practices

### 1. Test Your Patterns
Always use "Evaluate Regex" before saving to verify your pattern matches the intended assets.

### 2. Start Small
Begin with a specific pattern and expand it once you're confident it works correctly.

### 3. Use Descriptive Names
Your template names should clearly indicate their purpose for other team members.

### 4. Document Your Templates
Consider adding a description property to assets affected by templates explaining why they're configured this way.

### 5. Regular Review
Periodically review your templates to ensure they're still serving their intended purpose.

### 6. Coordinate with Your Team
Communicate template changes to avoid conflicts or confusion among team members.

## Tips and Tricks

### Pattern Writing Tips

- **Case Insensitive**: All patterns are case-insensitive, so `PROD` matches `prod`, `Prod`, etc.
- **Wildcards**: Use `.*` to match any characters
- **Specific Matches**: Use `^` and `$` to match exact names (e.g., `^CUSTOMERS$` matches only "CUSTOMERS")
- **Multiple Options**: Use `|` for OR conditions (e.g., `(PROD|PRODUCTION)_.*`)

### Property Management

- When "Overwrite properties" is OFF, templates add to existing properties
- When ON, templates replace all existing properties of the same type
- Properties added by templates show "Managed by Template [name]" in tooltips

### Performance Considerations

- Templates are applied immediately upon saving
- Large patterns affecting thousands of assets may take a moment to process
- The system prevents duplicate template names automatically

## Troubleshooting

### "Please fill out every field in the form"
Ensure you've:
- Entered a template name
- Provided a valid pattern
- Clicked "Evaluate Regex" to validate the pattern

### "Select at least one user to be the owner"
When "Approve assets" is enabled, you must specify an owner in the properties section.

### Pattern Not Matching Expected Assets
- Check for typos in your pattern
- Remember patterns are applied to the full asset path (database.schema.table)
- Use the preview feature to test different patterns
- Ensure you're using the correct wildcard syntax (`.*` not just `*`)

### Changes Not Appearing
- Refresh your browser to see the latest updates
- Check that your template was saved successfully
- Verify the affected assets in the main catalog view

## Advanced Features

### Combining Templates

Multiple templates can affect the same assets. When this happens:
- Properties and tags are combined from all applicable templates
- If "Overwrite properties" is enabled on any template, the most recently applied template takes precedence
- All selected quality checks from all templates are enabled

### Template Scope

Templates can affect various asset types in your catalog:
- **Database Objects**: Databases, schemas, tables, columns, functions
- **Tableau Assets**: Sites, projects, workbooks, views, datasources
- **Business Glossary**: Terms and metrics

Each asset type may have specific properties and checks available.

## Frequently Asked Questions

**Q: Can I rename a template after creating it?**
A: No, template names are permanent once created. You'll need to delete and recreate the template with a new name.

**Q: What happens when I delete a template?**
A: The template rule is removed, but any properties, tags, or checks already applied to assets remain unchanged.

**Q: Can multiple templates affect the same asset?**
A: Yes, multiple templates can apply to the same asset. Their effects are cumulative unless "Overwrite properties" is enabled.

**Q: How do I remove properties added by a template?**
A: You'll need to manually edit the affected assets or create a new template with "Overwrite properties" enabled to replace them.

**Q: Can I use templates on Tableau assets?**
A: Yes, templates work with Tableau sites, projects, workbooks, views, and datasources using the same pattern matching system.

**Q: Is there a limit to how many templates I can create?**
A: There's no hard limit, but for performance and manageability, it's best to create focused, purposeful templates rather than many overlapping ones.

Remember, templates are a powerful tool for maintaining a clean, well-organized data catalog. Used wisely, they can significantly improve your team's efficiency and data governance practices.