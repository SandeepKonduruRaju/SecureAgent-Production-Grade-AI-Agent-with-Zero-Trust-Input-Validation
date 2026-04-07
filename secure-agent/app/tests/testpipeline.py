# test_pipeline.py

from app.security.pipeline import run_security_pipeline

if __name__ == "__main__":
    user_input = input("Enter prompt: ")
    result = run_security_pipeline(user_input)
    print(result)