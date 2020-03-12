# Model_Deployment
ways to deploy a ML model into production

We would look at ways where we can 

1. Save the model developed on Jupyter notebook onto disk?
Ans: There are several ways to do this. Python has couple of libraries which can do this task
  
      1. Pickle
  
      2. Joblib
  
      [Example Code](https://nbviewer.jupyter.org/github/saianil58/Model_Deployment/blob/master/pickling.ipynb)

2. Can model learn(Re-Train) while on production ?
Ans: this is possible and only avialable with mininum algorithms. the Process is called Incremental Classification.
 [here]()is an example of the same using sklearn library and SGDClassifier
