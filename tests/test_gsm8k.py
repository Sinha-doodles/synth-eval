from syntheval.benchmarks.gsm8k import GSM8KVerifier

def test_gsm8k():
    sol = "The total apples is 5 + 3 = 8. #### 8"
    assert GSM8KVerifier.extract_final_number(sol) == "8"
