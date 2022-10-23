import pytest
# from adodbapi.is64bit import os
import os

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./testcases/allure-results -o ./allure-results/allure-report --clean')