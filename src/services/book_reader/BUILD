python_sources(
    name="app",
    sources=["app.py"],
)
docker_image(
    name="docker",
)


python_tests(
    name="tests",
    dependencies=[
        ":app",
        "//:tests"
    ]
)
