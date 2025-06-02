from dotenv import load_dotenv
import os

# docker -> ENV.PROPROTIES

env = "qa"
dotenv_path = f".env.{env}"
print(dotenv_path)
load_dotenv(dotenv_path, override=True)

profiles = os.getenv("profiles")
print(f"ENV: {env}, PROFILES: {profiles}")

env = "stg"
dotenv_path = f".env.{env}"
load_dotenv(dotenv_path, override=True)

profiles = os.getenv("profiles")
print(f"ENV: {env}, PROFILES: {profiles}")

env = "prd"
dotenv_path = f".env.{env}"
load_dotenv(dotenv_path, override=True)

profiles = os.getenv("profiles")
print(f"ENV: {env}, PROFILES: {profiles}")


env = "default"
dotenv_path = f".env.{env}"
load_dotenv(override=True)
profiles = os.getenv("profiles")
print(f"ENV: {env}, PROFILES: {profiles}")


# - AWS KMS 관련된 내용으로 처리 ( k8s secrets 도 가능 )
# - github secrets 사용 가능
# - git에서 actions를 통해 다른 private 레포에 권한을 주고 쓸 수 있음.