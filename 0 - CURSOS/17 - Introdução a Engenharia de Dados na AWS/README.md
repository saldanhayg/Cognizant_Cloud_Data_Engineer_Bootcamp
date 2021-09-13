#    Introdução a Engenharia de Dados na AWS

<h1>
   <img src="https://raw.githubusercontent.com/saldanhayg/Certificados/main/CURSOS/BI/ENGENHARIA%20DE%20DADOS/Introdu%C3%A7%C3%A3o%20a%20Engenharia%20de%20Dados%20na%20AWS.jpg" border="0">
</h1>

## Sobre: 

Conheça algumas das principais ferramentas para Engenharia de Dados disponíveis na Amazon Web Services (AWS). Nesse contexto, o expert explora os conceitos de ingestão, transformação e análise de dados em uma abordagem totalmente prática.

## Aulas desse curso

***Conheça os serviços da AWS*** 
<br>
Conheça os principais serviços oferecidos pela AWS no que diz respeito a Engenharia de Dados no domínio de Big Data.
<br>
<br>

***Mãos à obra*** 
<br>
Explore na prática alguns dos principais serviços oferecidos pela AWS para Big Data. Nesse sentido, o expert apresenta como utilizar essas ferramentas de forma efetiva.
<br>
<br>

## Instruções para atividade prática

### Kinesis Delivery Stream

- AWS Console -> Kinesis -> Create Firehose Delivery Stream "StreamName" -> Direct PUT -> Next -> Choose Destination -> Create S3 Bucket “covid-vaccines-logs-diolive” -> Configure settings -> buffer size 5mb -> buffer interval 60s -> IAM Role -> create new role -> Review and create

### EC2

- AWS Console -> EC2 -> Amazon Linux 2 AMI -> t2micro -> review and launch -> create new key pair -> download .pem file -> download putty -> puttygen -> load.pem file -> save .ppk file -> putty copy dns -> paste hostname -> SSH -> auth -> load ppk file -> login “ec2-user”

  - _sudo yum install -y aws-kinesis-agent_
  - _sudo yum install -y git_
  - _git clone https://tinyurl.com/64mf2mbu
  - _unzip Dataset.zip_
  - _chmod a+x LogGenerator.py_
  - _nano LogGenerator.py_
  - _less country_vaccinations.csv_
  - _sudo mkdir /var/log/diolive_
  - _cd /etc/aws-kinesis_
  - _sudo nano agent.json_
  - Copiar conteúdo do arquivo agent.json
  - agent.json -> "kinesis.endpoint": "kinesis.<region>.amazonaws.com"
  
- AWS Console -> EC2 -> Instances -> Select Instance -> Security -> Modify IAM Role -> Create New Role -> EC2 -> Administrator Access -> rolename “ec2-admin-role” -> save
  - _sudo service aws-kinesis-agent start_
  - _sudo chkconfig aws-kinesis-agent on_ (start with instance)
  - _cd ~_
  - _sudo ./LogGenerator.py 500000_
  - _tail -f /var/log/aws-kinesis-agent/aws-kinesis-agent.log_

### S3
- AWS Console -> S3 -> select bucket -> selecionar arquivo e download

### SSH EC2
  - _sudo service aws-kinesis-agent restart_
  - _sudo ./LogGenerator.py_
  - _tail -f /var/log/aws-kinesis-agent/aws-kinesis-agent.log_
  - AWS Console -> Kinesis Streams -> select stream -> monitoring
  
### AWS Glue
- AWS Console -> glue databrew -> create new project -> create new role -> create project
- Create dataset -> S3 -> formato CSV

## Link deste Bootcamp

 🎯 <a href="https://digitalinnovation.one/sign-up?ref=EDH1OJTU7E" target="_blank">Cognizant Cloud Data Engineer</a>
<br>
<br> 
***Cadastre-se no site para ter acesso a plataforma***


## Me siga nas redes sociais

👨‍💼🔮  https://linktr.ee/ygtecnologia 
<br>
<br> 
<br> 
“Investir em conhecimento rende sempre os melhores juros“. Benjamim Franklin
<br>
<br> 
🙏 Oração ! Foco ! Ação ! Yeshua Hamashia 