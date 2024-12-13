import os
import random
from datetime import datetime, timedelta
from git import Repo

# Đường dẫn đến repository Git (thư mục hiện tại)
repo_path = os.getcwd()

# Kiểm tra repository Git
if not os.path.exists(os.path.join(repo_path, ".git")):
    print("Không tìm thấy Git repository. Hãy khởi tạo bằng lệnh 'git init'")
    exit()

# Hàm tạo commit giả lập
def create_commit(repo, date):
    with open("data.txt", "w") as f:
        f.write(f"Commit on {date}\n")
    repo.index.add(["data.txt"])

    # Đặt biến môi trường để xác định ngày commit
    os.environ["GIT_AUTHOR_DATE"] = date.strftime("%Y-%m-%d %H:%M:%S")
    os.environ["GIT_COMMITTER_DATE"] = date.strftime("%Y-%m-%d %H:%M:%S")
    repo.index.commit(f"Commit on {date}")

# Hàm tạo nhiều commit
def make_commits(n):
    repo = Repo(repo_path)
    start_date = datetime(2019, 1, 1)
    end_date = datetime(2024, 12, 13)

    for _ in range(n):
        # Chọn ngày ngẫu nhiên trong khoảng thời gian
        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)

        print(f"Tạo commit vào ngày: {random_date}")
        create_commit(repo, random_date)

    # Push lên repository
    print("Đẩy các commit lên GitHub...")
    repo.git.push("origin", "main")

# Tạo 50000 commit giả lập
make_commits(50000)
