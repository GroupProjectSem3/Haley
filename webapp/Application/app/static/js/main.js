

    // // Load google charts
    // google.charts.load('current', {'packages':['corechart']});
    // // google.charts.load('49', {'packages': ['vegachart']}).then(drawChart);
    // google.charts.setOnLoadCallback(drawChart);

    // // Draw the chart and set the chart values
    // function drawChart() {
    // var data = google.visualization.arrayToDataTable([
    // ['Disease', 'Percentage'],
    // ['Covid', 80],
    // ['Diabetis', 15],
    // ['Flue', 5]
    // ]);

    // // Optional; add a title and set the width and height of the chart
    // var options = {'title':'Top 3 Diseases detected last month', 'width':400, 'height':500, is3D: true, backgroundColor: 'none',

    //     titleTextStyle: {
    //         color: '#E375D1',    // any HTML string color ('red', '#cc00cc')
    //         fontName: 'Lato', // i.e. 'Times New Roman'
    //         fontSize: '34px', // 12, 18 whatever you want (don't specify px)
    //         // bold: <boolean>,    // true or false
    //         // italic: <boolean>   // true of false
    //     }
    // }; 


    // // Display the chart inside the <div> element with id="piechart"
    // var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    // chart.draw(data, options);
    // }
    
    // window.onresize = doALoadOfStuff;

    // function doALoadOfStuff() {
    //     //do a load of stuff
    // }
/////////////////////////////////////////////////////////////////////////////////
// ********************************************************************************
    
    // // Load Charts and the corechart package.
    // google.charts.load('current', {'packages':['corechart']});

    // // Draw the pie chart for Sarah's pizza when Charts is loaded.
    // google.charts.setOnLoadCallback(drawDiseaseChart);

    // // Draw the pie chart for the Anthony's pizza when Charts is loaded.
    // google.charts.setOnLoadCallback(drawVisitsChart);

    // // Callback that draws the pie chart for Sarah's pizza.
    // function drawDiseaseChart() {

    //   // Create the data table for Disease.
    //   var data = new google.visualization.DataTable();
    //   data.addColumn('string', 'Disease');
    //   data.addColumn('number', 'Number of Cases');
    //   data.addRows([
    //     ['Covid', 79],
    //     ['Flue', 12],
    //     ['Diabetis', 7],
    //     ['Others', 2]
    //   ]);

    //   // Set options for Disease's pie chart.
    //   var options = {title:'Top Diseases diagnosed last month','width':400, 'height':500, is3D: true, backgroundColor: 'none',
    //                     titleTextStyle: {
    //                     color: '#E375D1',    // any HTML string color ('red', '#cc00cc')
    //                     fontName: 'Lato', // i.e. 'Times New Roman'
    //                     fontSize: '34px', // 12, 18 whatever you want (don't specify px)
    //                     }
                    
    //                 };

    //   // Instantiate and draw the chart for Disease's .
    //   var chart = new google.visualization.PieChart(document.getElementById('Disease_chart_div'));
    //   chart.draw(data, options);
    // }

    // // Callback that draws the pie chart for Visits's pizza.
    // function drawVisitsChart() {

    //   // Create the data table for Visits.
    //   var data = new google.visualization.DataTable();
    //   data.addColumn('string', 'Month');
    //   data.addColumn('number', 'No of Visits');
    //   data.addRows([
    //     ['Jan', 2],
    //     ['Feb', 2],
    //     ['Mar', 2],
    //     ['Apr', 0],
    //     ['May', 3]
    //     // ['Jun', 2],
    //     // ['Jul', 0],
    //     // ['Aug', 2],
    //     // ['Sep', 0],
    //     // ['Oct', 2],
    //     // ['Nov', 0],
    //   ]);

    //   // Set options for Visits's bar chart.
    //   var options = {title:'Your visits to Haley per month','width':800, 'height':500, is3D: true, backgroundColor: 'none',
    //                     titleTextStyle: {
    //                     color: '#E375D1',    // any HTML string color ('red', '#cc00cc')
    //                     fontName: 'Lato', // i.e. 'Times New Roman'
    //                     fontSize: '34px', // 12, 18 whatever you want (don't specify px)
    //                     }
                    
    //                 };

    //   // Instantiate and draw the chart for Visits.
    //   var chart = new google.visualization.ColumnChart(document.getElementById('Visits_chart_div'));
    //   chart.draw(data, options);
    // }

    // function resize () {
    //     // change dimensions if necessary
    //     chart.draw(data, options);
    // }
    // if (window.addEventListener) {
    //     window.addEventListener('resize', resize);
    // }
    // else {
    //     window.attachEvent('onresize', resize);
    // }