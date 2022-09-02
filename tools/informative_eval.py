import json
from math import isnan
from pathlib import Path

import pandas as pd
from sklearn.metrics import precision_recall_fscore_support

if __name__ == '__main__':
    pred = json.loads(Path('reviews/play_store_pred/a2dp.Vol.json').read_text())
    pred = {obj['id']: obj for obj in pred}
    data = pd.read_csv('informative_eval_1pass.csv', encoding='ISO8859-1').to_dict('records')
    data = [d for d in data if not isnan(d['manual'])]

    ypred = [d['informative'] for d in data]
    ylbl = [bool(pred[d['id']]['pred_informative']) for d in data]

    print(ypred)
    print(ylbl)

    precision, recall, f1score, support = precision_recall_fscore_support(ylbl, ypred, average='binary')
    print(f'Precision: {precision*100:.1f}%')
    print(f'Recall   : {recall*100:.1f}%')
    print(f'F1-score : {f1score*100:.1f}%')
    # print(f'Precision : {", ".join(f"{p*100:.1f}%" for p in precision)}')
    # print(f'Recall    : {", ".join(f"{p*100:.1f}%" for p in recall)}')
    # print(f'F1-score  : {", ".join(f"{p*100:.1f}%" for p in f1score)}')
