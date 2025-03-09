def pytest_control_run_step(step):
    print(step)
    assert  step["case_number"] == "TC-users-004"