function checkSameTeam(type) {
var Team1=document.getElementById("Team1").value;
var Team2=document.getElementById("Team2").value;
console.log(Team1)
console.log(Team2)
if(Team1==Team2){
		window.alert("you can't select the same team");
		document.getElementById("reset").click();
	}
}