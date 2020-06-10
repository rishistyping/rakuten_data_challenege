SORT_TSV_COL = "Integer_id"
TASK1_EVAL_COL = "Prdtypecode"
TASK2_EVAL_COL = "Image_id"

TASK1_PHASE1_PRED_FILENAME = "y_test_task1_phase1_pred.tsv"
TASK2_PHASE1_PRED_FILENAME = "y_test_task2_phase1_pred.tsv"
TASK1_PHASE2_PRED_FILENAME = "y_test_task1_phase2_pred.tsv"
TASK2_PHASE2_PRED_FILENAME = "y_test_task2_phase2_pred.tsv"

# Task evaluation
def evaluate_task_1(y_pred, y_test):
    y_test_array = np.array(y_pred[TASK1_EVAL_COL])
    y_pred_array = np.array(y_test[TASK1_EVAL_COL])

    score = f1_score(y_test_array, y_pred_array, average="macro")

    return score

def evaluate_task_2(y_pred, y_test):
    y_test_array = np.array(y_pred[TASK2_EVAL_COL])
    y_pred_array = np.array(y_test[TASK2_EVAL_COL])
    
    score = accuracy_score(y_test_array, y_pred_array)
    
    return score

def evaluate(team_id):
    # Loading the ground truth data for Task 1 and 2 of phase 1
    y_test_task1 = pd.read_table("{}/{}".format(GROUND_TRUTH_DIR, TASK1_PHASE1_TEST_FILENAME))
    y_test_task2 = pd.read_table("{}/{}".format(GROUND_TRUTH_DIR, TASK2_PHASE1_TEST_FILENAME))

    score_task1, score_task2 = None, None

    # This part of the script needs to be modifies based on the setup.
    try:
        y_pred_task1 = pd.read_table("{}/{}-{}".format(UPLOAD_DIR,team_id,TASK1_PHASE1_PRED_FILENAME)).sort_values(SORT_TSV_COL)
        score_task1 = evaluate_task_1(y_pred_task1, y_test_task1)
    except:
        pass #probably should do some smart sensing of what is wrong here

    try:
        y_pred_task2 = pd.read_table("{}/{}-{}".format(UPLOAD_DIR,team_id,TASK2_PHASE1_PRED_FILENAME)).sort_values(SORT_TSV_COL)
        score_task2 = evaluate_task_2(y_pred_task2, y_test_task2)
    except:
        pass

    return score_task1, score_task2

