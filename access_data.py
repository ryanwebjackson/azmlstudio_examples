from azureml import workspace

ws = Workspace(
  workspace_id='...',
  authorization_token='...'
)
ds = ws.datasets['datasetname']
frame = ds.to_dataframe()
