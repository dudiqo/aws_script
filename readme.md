<h1>Python script to pull resources data from AWS API Gateaway</h1>
<b>Initial setup:</b><br>
<ol>
    <li>AWS credentials file should be available on the local machine: ~/.aws/credentials (C:\Users\USER_NAME\.aws\credentials for Windows users)</li>
    <li>Required librariers: boto3, argparse, json, csv, pandas, os</li>
</ol>
<b>Documentation:</b><br>
Boto3 API Gataway<br>
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html<br>
Getting Started - AWS SDK for Python (Boto)<br>
https://aws.amazon.com/developers/getting-started/python/
<br><br>
<b>How to use:</b><br>
Available parameters:<br><ul>
    <li>-p (AWS credentials profile name; if not provided use default)</li>
    <li>-r (AWS region; mandatory)</li>
    <li>-m (HTTP methods to check; if not provided check all)</li>
    <li>-o (Output format: json, json-pretty, csv; if not provided generate json-pretty)</li>
</ul>
Sample use:<br>
<code>python resources.py -r us-east-1</code>