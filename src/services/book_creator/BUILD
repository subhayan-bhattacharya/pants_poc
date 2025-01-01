python_sources(
    name="app",
    sources=["app.py"],
)

docker_image(
    name="book-creator",
    source="Dockerfile",
    dependencies=[
        "src/services/utils:utils",
        "src/pants_poc/db:db",
        ":app"
    ]
)

python_tests(
    name="tests",
    dependencies=[
        ":app",
        "//:tests"
    ]
)
