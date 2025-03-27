# AWS Athena

To integrate Amazon Athena with Dot securely and efficiently, follow these steps to establish a connection, configure IAM permissions, and restrict access to specific Athena workgroups.

**1. Create a Dedicated IAM User for Dot**

For enhanced security, it's advisable to create a dedicated IAM user for Dot with permissions limited to the necessary Athena resources.

* **Create the IAM User**:
  * Sign in to the AWS Management Console.
  * Navigate to the IAM service.
  * Select "Users" and then "Add user".
  * Enter a username (e.g., `dot_athena_user`).
  * Choose "Programmatic access" to provide access via the AWS CLI, SDKs, or APIs.
* **Attach Policies**:
  * Select "Attach existing policies directly".
  * Attach the `AmazonAthenaFullAccess` managed policy to grant full access to Athena.
  * Attach the `AWSGlueConsoleFullAccess` policy to allow access to the AWS Glue Data Catalog, which Athena uses for metadata.
  * Ensure the user has the necessary permissions to access the relevant Amazon S3 buckets where your data resides.
* **Complete User Creation**:
  * Review the permissions and create the user.

**2. Optinonally restrict IAM Permissions to Specific Athena Workgroups**

To enhance security, you can limit the IAM user's permissions to specific Athena workgroups. This ensures Dot accesses only the intended resources.

* **Define the Policy**:
  * Create a custom IAM policy that grants permissions solely to the desired workgroups.
  * Specify the workgroup ARNs in the policy's `Resource` section.
* **Example Policy**:

```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "athena:StartQueryExecution",
          "athena:StopQueryExecution",
          "athena:GetQueryExecution",
          "athena:GetQueryResults"
        ],
        "Resource": [
          "arn:aws:athena:us-east-1:123456789012:workgroup/your_workgroup_name"
        ]
      },
      {
        "Effect": "Allow",
        "Action": [
          "glue:GetDatabase",
          "glue:GetTable",
          "glue:GetPartitions"
        ],
        "Resource": "*"
      },
      {
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:ListBucket"
        ],
        "Resource": [
          "arn:aws:s3:::your_bucket_name",
          "arn:aws:s3:::your_bucket_name/*"
        ]
      }
    ]
  }

```

 Replace `your_workgroup_name` with the name of your Athena workgroup and `your_bucket_name` with your S3 bucket name.

* **Attach the Policy**:
  * Navigate to the IAM console.
  * Select "Policies" and then "Create policy".
  * Use the JSON editor to input your custom policy.
  * Review and create the policy.
  * Attach this policy to the IAM user created for Dot.

For more details on controlling workgroup access with IAM policies, refer to the [AWS Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/workgroups-iam-policy.html).

**3. Configure Network Access**

Ensure that Dot can communicate with Athena by allowing outbound access to the following IP addresses, especially if your organization uses a firewall or network policies:

* `3.229.110.216`
* `3.122.135.165`

**4. Obtain the Access Key ID and Secret Access Key**

After creating the IAM user, generate the access keys required for programmatic access:

* **Generate Access Keys via AWS Management Console**:
  * In the IAM console, select "Users" and click on the username you created (e.g., `dot_athena_user`).
  * Navigate to the "Security credentials" tab.
  * In the "Access keys" section, click "Create access key".
  * Choose the appropriate use case (e.g., "Command Line Interface (CLI)") and click "Next".
  * Optionally, add a description tag for the access key, then click "Create access key".
  * The Access Key ID and Secret Access Key will be displayed. **This is the only time the Secret Access Key will be available**, so ensure you securely store it, either by downloading the `.csv` file or copying the keys to a secure location.

**5. Connect Dot to Amazon Athena**

With the IAM user and network configurations in place, proceed to connect Dot to Athena:

* Navigate to Dot's integration settings.
* Select "Add Integration" and choose Amazon Athena from the list of available data sources.
* Enter the Access Key ID and Secret Access Key of the IAM user created earlier.
* Specify the AWS region where your Athena instance is located.
* Provide any additional configuration details as prompted by Dot.

By following these steps, Dot will establish a secure connection to Amazon Athena, enabling efficient data access while adhering to security best practices.
