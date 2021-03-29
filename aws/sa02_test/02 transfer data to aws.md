# S3 transfer acceleration (TA)
Increase transfer speed by transferring
file to an AWS edge location which will
forward the data to the S3 bucket in the
target region

S3 TA is best for submitting data from client over the public internet

Compatible with multi-part upload

# Direct connect
Provides a dedicated private connection from a remote network to your VPC

Dedicated connection must be setup between your DC and AWS Direct
Connect locations

You need to setup a Virtual Private Gateway on your VPC

Benefit: 
* reduce costs
* increased bandwidth
* more consistent network 


Use Cases:
* Increase bandwidth throughput - working with large data sets – lower cost
* More consistent network experience - applications using real-time data feeds
* Hybrid Environments (on prem + cloud)

![img](02%20transfer%20data%20to%20aws/1.png)

Connection Types:
* Dedicated connections: 1Gbps-10Gbps
* Hosted connections: 50Mbps, 500Mbps, 10Gbps

Encryption:
* Data in transit is not encrypted but is
private
* AWS Direct Connect + VPN --> IPsec-encrypted private connection 


**Direct connect gateway**  
setup a Direct Connect to one or more VPC in many
different regions (same account)


# AWS VPN
comprised of 2 services:
* Aws Site-to-Site VPN: securely connect onpremises network to Amazon VPC
* AWS Client VPN: securely connect users to AWS or onpremise networks

Data transferred between your VPC and datacenter route over an encrypted VPN connection.

AWS Site-to-Site VPN enable you to create failover and CloudHub solutions with AWS Direct Connect
