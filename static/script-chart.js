
window.onload = function() {
    // var all_candidates = $("#candidates_total").text();
    var autosar_candidates = $("#candidates_autosar").text().substring(0,2);
    var ba_candidates = $("#candidates_ba").text().substring(0,2); 
    var c_candidates = $("#candidates_c").text().substring(0,2); 
    var devops_candidates = $("#candidates_devops").text().substring(0,2); 
    var frontend_candidates = $("#candidates_frontend").text().substring(0,2); 
    var ios_candidates = $("#candidates_ios").text().substring(0,2); 
    var java_candidates = $("#candidates_java").text().substring(0,2); 
    var net_candidates = $("#candidates_net").text().substring(0,2); 
    var python_candidates = $("#candidates_python").text().substring(0,2); 
    var qa_candidates = $("#candidates_qa").text().substring(0,2); 
    var status_inProcess = $("#status_process").text().substring(0,2);
    var status_standBy = $("#status_standby").text().substring(0,2);
    var status_passAllProcess = $("#status_pass").text().substring(0,2);
    var status_rejectedTechncalInterview = $("#status_tech").text().substring(0,2);
    var status_rejectedClientBUL = $("#status_bul").text().substring(0,2);
    var status_rejectedRecruiter = $("#status_recruiter").text().substring(0,2);
    var status_rejectedPreOffer =  $("#status_preoffer").text().substring(0,2);
    var status_rejectedOffer = $("#status_offer").text().substring(0,2);

    var ctx = document.getElementById("data-chart");
    var doughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
        labels: ["Autosar", "Business analyst", "C/C++", "DevOps","Frotend", "iOS", "Java", ".Net", "Phyton", "QA"],
        datasets: [
            {
            label: "Candidates profile",
            backgroundColor: ["#7FDBFF", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#FF851B","#2ECC40","#FFDC00","#0074D9","#85144b"],
            data: [autosar_candidates,ba_candidates,c_candidates,devops_candidates,frontend_candidates,ios_candidates,java_candidates,net_candidates,python_candidates,qa_candidates]
            }
        ]
        },
        options: {
            legend: {
                display: false},
            layout: {
            },    
        }
    })

    var ctx = document.getElementById("data-chart2");
    var doughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
        labels: ["In process", "Stand by", "Pass all process", "Rejected after technical interview","Rejected by BUL/Client", "Rejected by recruiter", "Rejected pre-offer", "Rejected offer"],
        datasets: [
            {
            label: "Candidates profile",
            backgroundColor: ["#7FDBFF", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#FF851B","#2ECC40","#FFDC00","#0074D9","#85144b"],
            data: [status_inProcess, status_standBy ,status_passAllProcess ,status_rejectedTechncalInterview ,status_rejectedClientBUL ,status_rejectedRecruiter ,status_rejectedPreOffer ,status_rejectedOffer ]
            }
        ]
        },
        options: {
            legend: {
                display: false},
            layout: {
            },    
        }
    })
  }

