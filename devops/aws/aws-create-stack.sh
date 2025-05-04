aws cloudformation create-stack \
  --stack-name CodeReimaginedTypingAppAWS \
  --template-body file://template.yaml \
  --parameters ParameterKey=DomainName,ParameterValue=codereimagined.com \
               ParameterKey=SubDomain,ParameterValue=typing \
               ParameterKey=HostedZoneId,ParameterValue=Z04459842AKUPNLFRWG1F \
               ParameterKey=CreateApex,ParameterValue=no
