from aws_cdk import (
    Stack,
)
from constructs import Construct

from aws_cdk.aws_lambda import Runtime

from aws_cdk import aws_lambda_python_alpha as lambda_python


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        new_function = lambda_python.PythonFunction(
            self, "royallePageLambda",
            runtime=Runtime.PYTHON_3_12,
            entry="lambda",
            handler="lambda_handler",
            index="royallepage.py"
        )
        group_function = lambda_python.PythonFunction(
            self, "groupLavoie",
            runtime=Runtime.PYTHON_3_12,
            entry="lambda",
            handler="lambda_handler",
            index="grouplavoie.py"
        )

        inscriptions_function = lambda_python.PythonFunction(
            self, "jollebite",
            runtime=Runtime.PYTHON_3_12,
            entry="lambda",
            handler="lambda_handler",
            index="inscriptions.py"
        )
