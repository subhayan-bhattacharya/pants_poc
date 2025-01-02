python_sources(
    name="app",
    sources=["./app.py"],
)
docker_image(
    name="docker",
)


python_test(
    source='./test_service.py',
    name="reader_tests",
    dependencies=[
        ":app",
        "//:tests"
    ]
)
