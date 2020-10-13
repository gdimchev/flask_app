{
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "inferenceAccelerators": [],
    "containerDefinitions": [
        {
            "name": "ecs-devops-sandbox",
            "image": "ecs-devops-sandbox-repository:00000",
            "resourceRequirements": null,
            "essential": true,
            "portMappings": [
                {
                    "containerPort": "8080",
                    "protocol": "tcp"
                }

            ]
        }
    ],
    "volumes": [],
    "networkMode": "awsvpc",
    "memory": "512",
    "cpu": "256",
    "executionRoleArn": "arn:aws:iam::<YOUR_AWS_ACCOUNT_ID>:role/ecs-devops-sandbox-execution-role",
    "family": "ecs-devops-sandbox-task-definition",
    "taskRoleArn": "",
    "placementConstraints": []
}