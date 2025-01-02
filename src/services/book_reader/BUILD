python_sources(
    name="app",
    sources=["app.py"],
)
docker_image(
    name="docker",
)


python_tests(
    name="reader_tests",
    dependencies=[
        ":app",
        "//:tests",
        "//:reqs1"
    ]
)
