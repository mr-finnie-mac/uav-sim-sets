Use train.csv for fitting, validation.csv for tuning, and test.csv for final scoring.
Inputs are ONLY the feature names in each manifest; sample/flight IDs and source row are metadata.
Never fit on evaluation/ truth/targets or unused samples. Test labels may be public for convenience.
Validation counts are additional acquired locations; budgets name training counts.
Paths contain acquired validation locations too; train.csv alone may omit intermediate path nodes.
Do not edit exported files: hard-linked identical test sets may share storage.
When sharing blind tests, exclude ALL evaluation/ directories and _shared/test_targets.csv files.
Reports are under reports/ in each case; HTML needs the root _assets/ folder alongside the cases.
