<html>
<head>
<title> Extraindo dados de um Banco de dados</title>
</head>
<body>
<b>Monitoramento | Arcelor Mittal Sistemas </b>
<button type="button" onClick="window.location.reload();">Refresh</button>
</br>
</br>

<?php
//Conexão com o banco de dados
$link = mysql_connect("localhost","adm","password");

//Seleciona o Banco de Dados
$conexao = mysql_select_db("temperatura"); if($conexao){

//query SQL
$strSQL = "SELECT max(tdate),max(ttime),info,value,ad 
           FROM dados2 
           
           ORDER BY tdate,ttime DESC";

//Executa a query(o recordset $rs contém o resultado da query)
$rs = mysql_query($strSQL);

echo '<table>';
echo '<tr>';
echo '<td>Hora</td>';
echo '<td>Data</td>';
echo '<td>Informação</td>';
echo '<td>Valor</td>';
echo '<td>AD []</td>';


while ($row = mysql_fetch_assoc($rs)){

// Escreve o valor da coluna Firstname(que está no array $row)
      
   echo '<tr>';
   echo '<td>'.$row["ttime"].'</td>';
   echo '<td>'.$row["tdate"].'</td>';
   echo '<td>'.$row["info"].'</td>';
   echo '<td>'.$row["value"].'</td>';
   echo '<td>'.$row["ad"].'</td>';
   echo '</tr>';
      
}

echo'</table>';

}

//Encerra a conexão
mysql_close();

?>


</body>

</html>

