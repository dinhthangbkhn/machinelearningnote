Amazon Data Lifecycle Manager (Amazon DLM) to automate the creation, retention, and deletion of snapshots taken to back up your Amazon EBS volumes. 
Combined with the monitoring features of Amazon CloudWatch Events and AWS CloudTrail, Amazon DLM provides a complete backup solution for EBS volumes at no additional cost.

**Route 53**  
Latency Routing lets Amazon Route 53 serve user requests from the AWS Region that provides the lowest latency. It does not, however, guarantee that users in the same geographic region will be served from the same location.

Geoproximity Routing lets Amazon Route 53 route traffic to your resources based on the geographic location of your users and your resources. You can also optionally choose to route more traffic or less to a given resource by specifying a value, known as a bias. A bias expands or shrinks the size of the geographic region from which traffic is routed to a resource.

Geolocation Routing lets you choose the resources that serve your traffic based on the geographic location of your users, meaning the location that DNS queries originate from.
Geolocation Routing is incorrect because you cannot control the coverage size from which traffic is routed to your instance in Geolocation Routing

Weighted Routing lets you associate multiple resources with a single domain name (tutorialsdojo.com) or subdomain name (subdomain.tutorialsdojo.com) and choose how much traffic is routed to each resource.

A: hostname to IPv4  
AAAA: hostname to IPv6  
CNAME: hostname to hostname  
Alias: hostname to AWS resource

After you create a hosted zone for your domain, such as example.com, you create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain.

Amazon Route 53 currently supports the following DNS record types:

- A (address record)

- AAAA (IPv6 address record)

- CNAME (canonical name record)

- CAA (certification authority authorization)

- MX (mail exchange record)

- NAPTR (name authority pointer record)

- NS (name server record)

- PTR (pointer record)

- SOA (start of authority record)

- SPF (sender policy framework)

- SRV (service locator)

- TXT (text record)

**Domain Name System Security Extensions (DNSSEC)**  
Domain Name System Security Extensions (DNSSEC) signing lets DNS resolvers validate that a DNS response came from Amazon Route 53 and has not been tampered with. When you use DNSSEC signing, every response for a hosted zone is signed using public-key cryptography.

Take note that DNSSEC is not a valid DNS record type. It is just a set of protocols that add a layer of security to the domain name system (DNS) lookup.

**SNS**  
You can use Amazon SNS message filtering to assign a filter policy to the topic subscription, and the subscriber will only receive a message that they are interested in.

**VPC Endpoint**  
enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection
you can attach an endpoint policy that controls access to the service to which you are connecting  

**Amazon EMR**  
Amazon EMR is a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS to process and analyze vast amounts of data.

**Amazon Redshift**  
allows you to run complex analytic queries against terabytes to petabytes of structured and semi-structured data, using sophisticated query optimization, columnar storage on high-performance storage, and massively parallel query execution.

**Redshift vs Dynamo response time**  
Amazon Redshift only delivers sub-second response times  
DynamoDB supports single-digit millisecond response times at any scale  

**AWS WAF**  
web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources.  
AWS WAF gives you control over how traffic reaches your applications by enabling you to create security rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that filter out specific traffic patterns you define.  
ou can deploy AWS WAF on Amazon CloudFront as part of your CDN solution, the Application Load Balancer that fronts your web servers or origin servers running on EC2, or Amazon API Gateway for your APIs.  
By using AWS WAF, you can configure web access control lists (Web ACLs) on your CloudFront distributions or Application Load Balancers to filter and block requests based on request signatures.  

**Amazon GuardDuty**  
Amazon GuardDuty is just a threat detection service

**Route53 and amazon S3**  
prerequisites for routing traffic to a website that is hosted in an Amazon S3 Bucket
* An S3 bucket that is configured to host a static website. The bucket must have the same name as your domain or subdomain. Ex: subdomain portal.tutorialsdojo.com, the name of the bucket must be portal.tutorialsdojo.com. (Amazon S3 can only serve static content. If you need to host dynamic content, you have to use an Amazon EC2 instance instead.)
* A registered domain name.
* Route 53 as the DNS service for the domain.

**Amazon EKS**  
Open source platform to migrate the application to a container service.
Applications running on Amazon EKS are fully compatible with applications running on any standard Kubernetes environment, whether running in on-premises data centers or public clouds.

**AWS Config**  
AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. 

By creating an AWS Config rule, you can enforce your ideal configuration in your AWS account

**Cloud Front**  
Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.

CloudFront is integrated with AWS – both physical locations that are directly connected to the AWS global infrastructure, as well as other AWS services. CloudFront works seamlessly with services including AWS Shield for DDoS mitigation, Amazon S3, Elastic Load Balancing or Amazon EC2 as origins for your applications, and Lambda@Edge to run custom code closer to customers’ users and to customize the user experience. Lastly, if you use AWS origins such as Amazon S3, Amazon EC2 or Elastic Load Balancing, you don’t pay for any data transferred between these services and CloudFront.

You can't store data in Amazon CloudFront. Technically, you only store cache data in CloudFront  


**VPC**  
you need to add IPv4 subnet first before you can create an IPv6 subnet.


**Snowball Edge**  
a type of Snowball device with on-board storage and compute power for select AWS capabilities. Snowball Edge can undertake local processing and edge-computing workloads in addition to transferring data between your local environment and the AWS Cloud.

**AWS Snowmobile**  
AWS Snowmobile is incorrect because this is an Exabyte-scale data transfer service used to move extremely large amounts of data to AWS. It is not suitable for transferring a small amount of data, like 80 TB in this scenario. You can transfer up to 100PB per Snowmobile

**object lock**  
Amazon EBS does not support object lock. Amazon S3 is the only service capable of locking objects to prevent an object from being deleted or overwritten.

**AWS Security Token Service (AWS STS)**  


**JSON Web Tokens**  
A JSON Web Token (JWT) is meant to be used for user authentication and session management.

**AWS SSO**  
Although the AWS SSO service uses STS, it does not issue short-lived credentials by itself. AWS Single Sign-On (SSO) is a cloud SSO service that makes it easy to centrally manage SSO access to multiple AWS accounts and business applications.


**Data Sync**  
you can transfer data from on-premises directly to Amazon S3 Glacier Deep Archive

**Snow mobile**  
Snowmobile is more suitable if you need to move extremely large amounts of data to AWS or need to transfer up to 100PB of data. This will be transported on a 45-foot long ruggedized shipping container, pulled by a semi-trailer truck. Take note that you only need to migrate 250 TB of data, hence, this is not the most suitable and cost-effective solution.


**Connection between EC2 instances and RDS**  
You can use Secure Sockets Layer (SSL) to encrypt connections between your client applications and your Amazon RDS DB instances running Microsoft SQL Server.  
When you create an SQL Server DB instance, Amazon RDS creates an SSL certificate for it  
There are 2 ways to use SSL to connect to your SQL Server DB instance:  
* Force SSL for all connection: this happens transparently to the client, and the client doesn't have to do any work to use SSL.
* Encrypt specific connections: this sets up an SSL connection from a specific client computer, and you must do work on the client to encrypt connections.

**Cloud Formation**  
a template is a JSON or a YAML-formatted text file that describes your AWS infrastructure 
The Resources section is the only required section  

**EC2-Placement groups**  
* It is recommended that you launch the number of instances that you need in the placement group in a single launch request 
* use the same instance type for all instances in the placement group

If you try to add more instances to the placement group later, or if you try to launch more than one instance type in the placement group, you increase your chances of getting an insufficient capacity error.  

If you stop an instance in a placement group and then start it again, it still runs in the placement group. However, the start fails if there isn't enough capacity for the instance.

If you receive a capacity error when launching an instance in a placement group that already has running instances, stop and start all of the instances in the placement group, and try the launch again. Restarting the instances may migrate them to hardware that has capacity for all the requested instances.

**EC2-Remote Desktop connection**
Since you are using a Remote Desktop connection to access your EC2 instance, you have to ensure that the Remote Desktop Protocol is allowed in the security group. By default, the server listens on TCP port 3389 and UDP port 3389.

**EC2-Reserved Instance Marketplace**   
Reserved Instance Marketplace is a platform that supports the sale of third-party and AWS customers' unused Standard Reserved Instances, which vary in terms of length and pricing options

**Enhanced networking**  
* uses single root I/O virtualization (SR-IOV: higher I/O performance and lower CPU utilization) to provide high-performance networking capabilities on supported instance types  
* Enhanced networking provides higher bandwidth, higher packet per second (PPS) performance, and consistently lower inter-instance latencies  
* There is no additional charge for using enhanced networking.

**Elastic IP**  
An Elastic IP address doesn’t incur charges as long as the following conditions are true:
* Elastic IP address is associated with an Amazon EC2 instance.
* instance associated with the Elastic IP address is running
* instance has only one Elastic IP address attached to it.  
* If you’ve stopped or terminated an EC2 instance with an associated Elastic IP address and you don’t need that Elastic IP address anymore, consider disassociating or releasing the Elastic IP address

**Network Load Balancer**  
best suited for load balancing of TCP traffic where extreme performance is required

**Auroza**  
Amazon Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases.  
The read replication latency of less than 1 second is only possible if you would use Amazon Aurora replicas. Aurora replicas are independent endpoints in an Aurora DB cluster, best used for scaling read operations and increasing availability. You can create up to 15 replicas within an AWS Region.

**S3 multipart**  
slow upload time of the video objects to Amazon S3. To address this issue, you can use Multipart upload in S3 to improve the throughput. It allows you to upload parts of your object in parallel thus, decreasing the time it takes to upload big objects.  
Using multipart upload provides the following advantages:

* Improved throughput - You can upload parts in parallel to improve throughput.

* Quick recovery from any network issues - Smaller part size minimizes the impact of restarting a failed upload due to a network error.

* Pause and resume object uploads - You can upload object parts over time. Once you initiate a multipart upload, there is no expiry; you must explicitly complete or abort the multipart upload.

* Begin an upload before you know the final object size - You can upload an object as you are creating it.


**web identity federation**  
don't need to create custom sign-in code or manage your own user identities. Instead, users of your app can sign in using a well-known identity provider (IdP) —such as Login with Amazon, Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP, receive an authentication token, and then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions to use the resources in your AWS account

**IAM cross-account**  
can use an IAM role to delegate access to resources that are in different AWS accounts that you own. You share resources in one account with users in a different account. By setting up cross-account access in this way, you don't need to create individual IAM users in each account. In addition, users don't have to sign out of one account and sign into another in order to access resources that are in different AWS accounts.