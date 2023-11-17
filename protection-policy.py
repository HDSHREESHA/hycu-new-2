import boto3

session = boto3.Session(
    aws_access_key_id = "ASIAZYW655GOXX3WQURL",
    aws_secret_access_key = "SRNim5M4FmTTo/OeLbGIT3gKAcE6Ao6JzfWefNVU",
    aws_session_token = "IQoJb3JpZ2luX2VjEBAaCXVzLWVhc3QtMSJGMEQCIF6sca3/MvQ4pTA3K2leBFxfzpyFZ1mCGNxKlurJ8M/3AiAkL8ljm7gmpwuMfmaiHAO4dbFen+jz3NpvEBfSSaUVsyqmAgg5EAEaDDY3MTU1NjE2ODA5MyIM+AL5T6pBLkVwBiNSKoMCFjlsdA2zBlwXK+r8FBwE2qBE5C/CXYHBt0+GwSebaVhMdD9HUgGVzWDjmFFYXtZEdLR5HI3Cv7oAA1MvIPi2XXi4VI08tZzYVMtrsEft59YaxuyXAZer1DHLkAOSajPweAtqAGdZ3H29DLFcbYB2eNvvCPSEfye6k64uPYQyukWx6oOVgiZrB4PSv2dz8ma1VsHPChPQYPORhrxu0toSCvs54mQh7hpwmTvPrAZRPaP1ZtvJ/FzNbe5D93uN3tcgXOHxc6y3Ibb4/vdULtd2iFZAM9qiwIZ5S8KGkKI1+hflFNUxQdeB0aeuieyB0xsj4ypoErbBPi6TKadkklsSPTk2AzCIktypBjqeAU00Db4EIjHU5DJ9eMzjknpcEStbikTELf1rf4EY0N83ilOwrJtKRGZxIxZDyUx+szSirANjVCzR7sQlmSvDUZAqSsSmbMrA2YepC3ugX6xPPG6r1fDARmJE18jmXmduHLaaH2dHqQ77cFxTemCjGj/LwZGIZWt5hKtb6k3TtY0o2XqdtrQ7BGlpyAQvKbRqy1yGUP9ieKlvfZkGeWWK",
    region_name = "us-west-1"
)
client = session.client('cloudformation')
params = {
    "StackStatusFilter": [
        "CREATE_FAILED",
        "CREATE_COMPLETE",
        "ROLLBACK_FAILED",
        "ROLLBACK_COMPLETE",
        "DELETE_FAILED",
        "DELETE_COMPLETE",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
        "UPDATE_ROLLBACK_FAILED",
        "UPDATE_ROLLBACK_COMPLETE",
        "IMPORT_COMPLETE",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_COMPLETE"
    ]
}
response = client.list_stacks(**params)

print(response)
