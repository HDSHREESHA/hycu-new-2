import boto3

session = boto3.Session(
    aws_access_key_id = "ASIA3B5BC4RWPS7BIV43",
    aws_secret_access_key = "1twEuiA65sv/5KWENn1EdWmoS/ZnWY1tsYtYNGeP",
    aws_session_token = "IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJIMEYCIQC/HOGa9i4y3j5stGZpWE8C2nVIYtgCjIPOgyCJoDvGnwIhAKeJPQGav1CkAL1fGeSVngV8Dk3pSt94WHSZAaam3XRJKqYCCHoQABoMNzYwMDEwMTcxNTAwIgws0+25zRRhOiBG67QqgwI6LgBTllRvlAOO5NJZWP49AeTHlD/J6UQKaCNXtWBA1oizApHxb2p736owFUuj58+Pk3loy8z8V3/jLctGW6IMzf8Mqmueaf1+QjblYcHriVbyci+sxBJfbLheJoz3y80/eR//39wOOqEl04XQ8VZGKa1/VEVW6m76rJXfc1mE7m+cYoBbicKQibBLohtxKsRDYMICFkQjpllH540JM68Xd0ZjVUMJynTwUt4u+XYNfxE7v8eAnscYhBzf5WjG2u82fI87OpYVIssEXIT2KrXI0uPV+9hRlBpIyW+UajqeaQhdbSvopLOBd2GGLLbxzlDMW/TEzK6cQCZfo/+7yWKahNfVMJ7KtakGOpwBpStGKt9LBYn3oWxePNrQDCkMRyDJpd/JLI7kGFHBDe9zvlAfLPtfqvFMXcoz17PafTMv/32ZN0n5z5pE5X0iQorlg2rk8ZacPe7GYX3wOVYmDBy4R+IO984AkzVoVKNWD2oEP323+tesbkJ+FSUFhCw5mlW2MygyZH5k2W0WWGzq/ExgqyxQbZvnctsp7nSn7kws/cWVoY41XjPE",
    region_name = "eu-north-1"
)


client = session.client('cloudformation')

# Replace 'YourStackSetName' with the name of your StackSet
stack_set_name = 'StackSet1'

# Step 1: List StackSet operations
response = client.list_stack_set_operations(StackSetName=stack_set_name)

# Get the latest operation ID
latest_operation_id = response['Summaries'][0]['OperationId']


# Step 2: Describe the latest operation
latest_operation = client.list_stack_set_operation_results(
    StackSetName=stack_set_name,
    OperationId=latest_operation_id
)

# Print the details of the latest operation
print(latest_operation)