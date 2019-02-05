$(document).ready(function(){
					$("#filter").load("filter.html");
					$("#jobs").load("job-listing.html");
					$("#job-description").load("ad.html");
					var x = window.matchMedia("(max-width: 700px)")
					if (x.matches) {
						$("#").click(function(){
							$("#job-description").load("job-des.html");
						});
					}
					$("#close").click(function()
					{
						$("#popup").remove();
					}
				);
				});

				
				function load_des()
				{
					$("#job-description").load("job-des.html");
				}
				function login(){
					$("#popup-div").load("log.html");
					document.getElementById("popup").style.display="block";
				}
				function close_div()
				{
					$("#popup-div").empty();
					document.getElementById("popup").style.display="none";
				}
				function close_des()
				{
					$("#job-description").empty();
					$("#job-description").load("ad.html");
				}
				function register(){
					$("#popup-div").load("reg.html");
					document.getElementById("popup").style.display="block";

				}
				function category()
				{
					$("#popup-div").load("cat.html");
					document.getElementById("popup").style.display="block";
				}
				function location_12()
				{
					$("#popup-div").load("location.html");
					document.getElementById("popup").style.display="block";
				}
				function search_btn(x)
									{
										document.getElementById("search_btn").style.display="none";
										document.getElementById("search_candidates").style.display="block";
										document.getElementById("search_jobs").style.display="block";
									}
									function change_color(x)
									{
										x.style.color='white';
										x.style.backgroundColor= '#4a4d4e';
									}