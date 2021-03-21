import boto3
ec2 = boto3.resource('ec2', region_name = 'eu-west-2')

# create a file to store the key locally
outfile = open('ec2-keypair4.pem','w')

# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2-keypair4')

# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)
