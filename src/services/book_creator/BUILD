python_sources(
    name="app",
    sources=["app.py"],
)

files(
    name="service_files",
    sources=["**/*.py"]
)

docker_image(
    name="book-creator",
    source="Dockerfile",
    dependencies=[
        "src/services/utils:util_files",
        ":service_files",
        "//:root",
#        "//:git"
    ]
)

python_tests(
    name="tests",
    dependencies=[
        ":app",
        "//:tests"
    ]
)
