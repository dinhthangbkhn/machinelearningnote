# Practice test 1

**AWS Resource Access Manager (RAM)** is a service that enables you to easily and securely share AWS resources with any AWS account or within your AWS Organization. You can share AWS Transit Gateways, Subnets, AWS License Manager configurations, and Amazon Route 53 Resolver rules resources with RAM.

RAM eliminates the need to create duplicate resources in multiple accounts, reducing the operational overhead of managing those resources in every single account you own.

**AWS Organizations** is an account management service that lets you consolidate multiple AWS accounts into an organization that you create and centrally manage. With Organizations, you can create member accounts and invite existing accounts to join your organization. You can organize those accounts into groups and attach policy-based controls.

**AWS Control Tower** simply offers the easiest way to set up and govern a new, secure, multi-account AWS environment. This is not the most suitable service to use to securely share your resources across AWS accounts or within your Organization.


**AWS ParallelCluster** is simply an AWS-supported open-source cluster management tool that makes it easy for you to deploy and manage High-Performance Computing (HPC) clusters on AWS


![img](practice_test1_folder/1.png)
 
**io1** volume allows you to specify a consistent IOPS rate when you create the volume

**General Purpose SSD (gp2)** is a type of SSD that can handle small, random I/O operations, the Provisioned IOPS SSD volumes are much more suitable to meet the needs of I/O-intensive database workloads such as MongoDB, Oracle, MySQL, and many others.

**HDD volumes** (such as Throughput Optimized HDD and Cold HDD volumes) are more suitable for workloads with large, sequential I/O operations instead of small, random I/O operations.

**Amazon RDS Multi-AZ**:  
When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable.

In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of Amazon Aurora), so that you can resume database operations as soon as the failover is complete. Since the endpoint for your DB Instance remains the same after a failover, your application can resume database operation without the need for manual administrative intervention.

**Oracle RMAN and RAC** are not supported in RDS.

**Use signed URLs** for the following cases:

- You want to use an RTMP distribution. Signed cookies aren't supported for RTMP distributions.

- You want to restrict access to individual files, for example, an installation download for your application.

- Your users are using a client (for example, a custom HTTP client) that doesn't support cookies.

**Use signed cookies** for the following cases:

- You want to provide access to multiple restricted files, for example, all of the files for a video in HLS format or all of the files in the subscribers' area of a website.

- You don't want to change your current URLs.

**Field-Level Encryption** only allows you to securely upload user-submitted sensitive information to your web servers.

**Amazon Aurora Serverless**is an on-demand, auto-scaling configuration for Amazon Aurora. An **Aurora Serverless DB cluster** is a DB cluster that automatically starts up, shuts down, and scales up or down its compute capacity based on your application's needs. Aurora Serverless provides a relatively simple, cost-effective option for infrequent, intermittent, sporadic or unpredictable workloads. It can provide this because it automatically starts up, scales compute capacity to match your application's usage and shuts down when it's not in use.

Take note that a **non-Serverless DB cluster for Aurora** is called a **provisioned DB cluster**. **Aurora Serverless clusters and provisioned clusters** both have the same kind of high-capacity, distributed, and highly available storage volume.

When you work with **Amazon Aurora without Aurora Serverless (provisioned DB clusters)**, you can choose your DB instance class size and create Aurora Replicas to increase read throughput. This model works well when the database workload is predictable, because you can adjust capacity manually based on the expected workload.

With **Aurora Serverless** , you can create a database endpoint without specifying the DB instance class size. You set the minimum and maximum capacity

**Amazon Redshift data warehouse cluster with Concurrency Scaling**: this type of database is primarily used for **online analytical processing (OLAP)** and not for **online transactional processing (OLTP)**. Concurrency Scaling is simply an Amazon Redshift feature that automatically and elastically scales query processing power of your Redshift cluster to provide consistently fast performance for hundreds of concurrent queries.

![img](practice_test1_folder/2.png)

**AWS X-RAY**: helps you debug and analyze your microservices applications with request tracing so you can find the root cause of issues and performance.

**Amazon CloudWatch** has available Amazon EC2 Metrics for you to use for monitoring CPU utilization, Network utilization, Disk performance, and Disk Reads/Writes. In case you need to monitor the below items, you need to prepare a custom metric using a Perl or other shell script, as there are no ready to use metrics for:

Memory utilization

Disk swap utilization

Disk space utilization

Page file utilization

Log collection

**Enhanced Monitoring** is a feature of Amazon RDS. By default, Enhanced Monitoring metrics are stored for 30 days in the CloudWatch Logs.

**Amazon FSx for Windows File Server** provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system. Amazon FSx for Windows File Server has the features, performance, and compatibility to easily lift and shift enterprise applications to the AWS Cloud

**AWS Storage Gateway** is primarily used to integrate your on-premises network to AWS but not for migrating your applications. Using a file share in Storage Gateway implies that you will still keep your on-premises systems, and not entirely migrate it.

You can authenticate to your DB instance using **AWS Identity and Access Management (IAM) database authentication**. IAM database authentication works with **MySQL and PostgreSQL**. With this authentication method, you don't need to use a password when you connect to a DB instance. Instead, you use an authentication token.

IAM database authentication provides the following benefits:
* Network traffic to and from the database is encrypted using Secure Sockets Layer (SSL)
* can use IAM to centrally manage access to your database resources, instead of managing access individually on each DB instance.


The maximum days for the EFS lifecycle policy is only 90 days


**Amazon Macie** is an ML-powered security service that helps you prevent data loss by automatically discovering, classifying, and protecting sensitive data stored in Amazon S3. Amazon Macie uses machine learning to recognize sensitive data such as personally identifiable information (PII) or intellectual property, assigns a business value, and provides visibility into where this data is stored and how it is being used in your organization.