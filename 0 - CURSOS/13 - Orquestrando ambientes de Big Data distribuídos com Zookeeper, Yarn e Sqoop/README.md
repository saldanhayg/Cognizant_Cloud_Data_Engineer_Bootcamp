# 💻   Orquestrando ambientes de Big Data distribuídos com Zookeeper, Yarn e Sqoop

<h1>
   <img src="https://tinyurl.com/49pdxe6e" border="0">
</h1>

Explore algumas das principais ferramentas relacionadas à plataforma Hadoop. Nesse contexto, aprenda mais sobre Zookeeper para gerenciar sistemas distribuídos e Sqoop para transferir informações entre bancos de dados relacionais. Além disso, conheça o YARN (Yet Another Resource Negotiator), um elemento central da arquitetura do Hadoop para o gerenciamento de recursos

## Sobre: 

Tópicos co curso :<br>
✔  **Conhecendo o ambiente do Sqoop**<br>
✔  **O que é Zookeeper e Sqoop**<br>

<h2>
   <img src="https://i.ibb.co/pRHqY8q/1.jpg" alt="1" border="0">
</h2>
<br>
<h2>
   <img src="https://i.ibb.co/YXfVRvw/2.jpg" alt="2" border="0"> 
</h2>
<br>
<h2>
   <img src="https://i.ibb.co/N9XbdWR/3.jpg" alt="3" border="0">
</h2>
<br>


## Lista de Comandos 

sudo service hadoop-hdfs-namenode start<br>
sudo service hadoop-hdfs-secondarynamenode start<br>
sudo service hadoop-hdfs-datanode start<br>
sudo service hadoop-yarn-nodemanager start<br>
sudo service hadoop-yarn-resourcemanager start<br>
sudo service hadoop-mapreduce-historyserver start<br>
sudo service zookeeper-server start<br>
<br>
-----------------------------------------------------------------------------------------------<br>
sh install_sqoop.sh<br>
mysql -u root -h localhost -pEveris@2021 < pokemon.sql<br>
sh sqoop_import.sh<br>
hdfs dfs -text /user/everis-bigdata/pokemon/*.gz |more<br>

hdfs dfs- cat /user/everis-bigdata/pokemon/1/*<br>
<br>
-----------------------------------------------------------------------------------------------<br>
sudo yum install --assumeyes sqoop<br>
cd /tmp<br>
wget http://www.java2s.com/Code/JarDownload/java-json/java-json.jar.zip<br>
unzip /tmp/java-json.jar.zip<br>
sudo mv /tmp/java-json.jar /usr/lib/sqoop/lib/<br>
sudo chown root: /usr/lib/sqoop/lib/java-json.jar<br>
sqoop-version<br>
<br>
---------------------------------------Selec-------------------------------------------<br>
sudo -u hdfs hdfs dfs -rm -R /user/everis-bigdata/pokemon<br>
<br>
sudo -u hdfs sqoop import \<br>
--connect jdbc:mysql://localhost/trainning \<br>
--username root --password "Everis@2021" \<br>
--fields-terminated-by "|" \<br>
--split-by Generation \<br>
--target-dir /user/everis-bigdata/pokemon \<br>
--query 'SELECT * FROM pokemon WHERE $CONDITIONS' \<br>
--where 'Number IS NOT NULL' \<br>
--compress \<br>
--num-mappers 4<br>
<br>


## Link deste curso  💻

 🎯 <a href="https://digitalinnovation.one/cursos/orquestrando-ambientes-de-big-data-distribuidos-com-zookeeper-yarn-e-sqoop?ref=certificate/36E78B2D" target="_blank">Orquestrando ambientes de Big Data distribuídos com Zookeeper, Yarn e Sqoop</a>

<br>
<br>
[Me siga nas redes sociais](https://linktr.ee/ygtecnologia)
<br>
<br> 
🙏 Oração ! Foco ! Ação ! Jeova Jireh - Deus Provera 🙏  
