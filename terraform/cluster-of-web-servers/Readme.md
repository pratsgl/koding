# Sample Project based on following blog :

https://blog.gruntwork.io/an-introduction-to-terraform-f17df9c6d180
https://github.com/gruntwork-io/intro-to-terraform/tree/master/cluster-of-web-servers

resource "aws_autoscaling_group" 	# CREATE THE AUTO SCALING GROUP
resource "aws_elb"   				# CREATE AN ELB TO ROUTE TRAFFIC ACROSS THE AUTO SCALING GROUP
resource "aws_launch_configuration" # CREATE A LAUNCH CONFIGURATION THAT DEFINES EACH EC2 INSTANCE IN THE ASG
resource "aws_security_group" 		# CREATE THE SECURITY GROUP THAT'S APPLIED TO EACH EC2 INSTANCE IN THE ASG
resource "aws_security_group"  		# CREATE A SECURITY GROUP THAT CONTROLS WHAT TRAFFIC AN GO IN AND OUT OF THE ELB

###########
mode : data
"type":"aws_availability_zones",
"name":"all"

mode : managed
"type":"aws_autoscaling_group",
"name":"example",

"mode":"managed"
"type":"aws_elb"
"name":"example",

"mode":"managed",
"type":"aws_instance",
"name":"busybox-ec2"

"mode":"managed",
"type":"aws_launch_configuration",
"name":"example",


"mode":"managed",
"type":"aws_security_group",
"name":"busyboxvpc",

"mode":"managed",
"type":"aws_security_group",
"name":"elb",

"mode":"managed",
"type":"aws_security_group",
"name":"instance",

#### EOF #####
