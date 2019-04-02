// Empty JS for your own code to be here


/* $.ajax({
	url : "http://localhost:8080/login",
	data : JSON.stringify({
		username : username,
		password : password
	}),
	contentType : 'application/json',
	//processData : false,
	type : 'POST',
	success : function(data) {

		if(data == "true"){
			window.location.href="http://localhost:8080/ChangeAnalyzerInput.html";
		}else{
			alert('invalid username / password');
		}
	},
	error : function(e) {
		alert("error: "+e);
	}
});*/



//
//var noOfRows = 1;
//var id;
//	var name;
//	var classid;
//	var createdon;
//	var updatedon;
//	var action;
//
//// function to add a new row for searching multiple bitbucket repositories
//function addrow(){
//
//	noOfRows++;
//
//	//create new row in the bitbucket table
//
//	var row = usertable.insertRow(1);
//
//
//	// Read data from the textboxes for bitbucket search
//	//var txtProj = document.getElementById('projectkey').value;
//	//var txtRepo = document.getElementById('reponame').value;
//	//var txtCDFrom = document.getElementById('fromcommitid').value;
//	//var txtCD = document.getElementById('tocommitid').value;
//
//	// Insert new cells (<td> elements)
//	//id = row.insertCell(0);
//	 name = row.insertCell(1);
//	 //classid = row.insertCell(2);
//	 //createdon = row.insertCell(3);
//	 //updatedon = row.insertCell(4);
// action = row.insertCell(5);
//
//	// Add the text to the new cells display in the table
//	id.innerHTML = "1";
//name.innerHTML = "<input type='text' class='form-control' id='name'/>";
//	classid.innerHTML = "<input type='text' class='form-control' id='classid'/>";
//	createdon.innerHTML = "<input type='text' class='form-control' id='createdon'/>";
//updatedon.innerHTML = "<input type='text' class='form-control' id='updatedon'/>";
//action.innerHTML = "<button type='button' onclick='save()' class='btn btn-success'>Save</button>";
//}
//
//function save(){
//console.log(document.getElementById('classid').value);
//name.innerHTML ="diHEwg";
//	classid.innerHTML = "test";
//	createdon.innerHTML = "value";
//updatedon.innerHTML = "value";
//action.innerHTML = "<button type='button' onclick='update()' class='btn btn-success'>Update</button><button type='button' onclick='save()' class='btn btn-success'>Delete</button>";
//
//}


<script>
$.ajax({
	url : "http://localhost:5000/insert",
	data : JSON.stringify({
		name : name
	}),
	contentType : 'application/json',
	type : 'POST',
	success : function(data) {
console.log(data);
	},
	error : function(e) {
		console.log("error: "+e);
	}
	console.log(row);





	 id = row.insertCell(0);
	 name1 = row.insertCell(1);
	 classid = row.insertCell(2);
	 createdon = row.insertCell(3);
	 updatedon = row.insertCell(4);
	action = row.insertCell(5);
	// Add the text to the new cells display in the table
	id.innerHTML = "<input type='text' class='form-control' id='id'/>";
	name1.innerHTML = "<input type='text' class='form-control' id='name'/>";
	classid.innerHTML = "<input type='text' class='form-control' id='classid'/>";
	createdon.innerHTML = "<input type='text' class='form-control' id='createdon'/>";
	updatedon.innerHTML = "<input type='text' class='form-control' id='updatedon'/>";
action.innerHTML = "<button type='button' onclick='POST' class='btn btn-success'>Save</button>";
}

<!--function save(){-->
<!--console.log(document.getElementById('classid').value);-->
	<!--id.innerHTML = "1";-->
	<!--name1.innerHTML ="YY";-->
	<!--classid.innerHTML = "mm";-->
	<!--createdon.innerHTML = "value";-->
<!--updatedon.innerHTML = "value";-->
<!--action.innerHTML = "<button type='button' onclick='update()' class='btn btn-success'>Update</button><button type='button' onclick='del()' class='btn btn-success'>Delete</button>";-->

<!--}-->

				</script>




<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Data Labs</title>

    <meta name="description" content="Source code generated using layoutit.com">
    <meta name="author" content="LayoutIt!">
	<script src="static/jquery.min.js"></script>
    <script src="static/bootstrap.min.js"></script>
    <link href="static/bootstrap.min.css" rel="stylesheet">
    <link href="static/style.css" rel="stylesheet">

  </head>
  <body>
<form method="POST" action="">
	<input type="text" name="name"/>
	<input type="submit" value="ADD"/>
</form>


    <div class="container-fluid">
	<div class="row">
		<div class="col-md-12">
			<h3>
				DataLabs
			</h3>

			<table class="table">

				<thead>
					<tr>
						<th>
							ID
						</th>
						<th>
							Name
						</th>
						<th>
							Class Id
						</th>
						<th>
							Created On
						</th>
						<th>
							Updated On
						</th>
						<th>
							Action
						</th>
					</tr>
				</thead>
				{% for user in Data1 %}
				<tbody>
				<tr>
					<td>
						{{user.id}}
					</td>
					<td>
						{{user.name}}
					</td>
					<td>
						{{user.class_id}}
					</td>
					<td>
						{{user.created_on}}
					</td>
					<td>
						{{user.updated_on}}
					</td>
					<td>
							<button type="button" class="btn btn-success">
								Update
							</button>
							<button type="button" class="btn btn-success">
								Delete
							</button>
						</td>


				</tr>
				</tbody>
				{% endfor %}

			</table>

		</div>
	</div>
</div>


  </body>
</html>