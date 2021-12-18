window.onload = async function() {
    var $table = $('#table');

    let mydata = await fetch("https://nexgenfinal.uc.r.appspot.com/all_data")
        .then(response => response.json())

    $(function () {
        $('#table').bootstrapTable({
            data: mydata
        });
        $('#table').DataTable();
    });

    // console.log(mydata)

    ChartBar(mydata, 'chart1');
    ChartPie(mydata, 'chart2');
    BubbleChart(mydata, 'air_temp', 'wind_speed', 'frostbite', 'chart4');

}

function BubbleChart(mydata, attr1, attr2, attr3, chartid) {
    all_data = [];
    labels = ['glove1', 'glove2', 'glove3', 'glove4']
    colors = []
    var myColor = d3.scaleOrdinal().domain(labels)
    .range(d3.schemeSet2)
    for (val of labels) {
      colors.push(myColor(val))
    }
    let count=0;
    
    for(label of labels){
        all = mydata.filter(function(d){ return d.glove == label });
        glove_data = [];
        let limit = 5;
        for (row of all) {
            if (limit > 0) {
                glove_data.push({
                    x: row[attr1], 
                    y:row[attr2], 
                    r: Math.round((row[attr3] / 6) * 100) / 100                    
                })
            }
            limit = limit - 1;
        }
        all_data.push({
            label: label, 
            data: glove_data, 
            backgroundColor: colors[count]
        })
        count = count + 1;
    }
    
    const data = {datasets: all_data};

    var chart = new Chart(chartid, {
        type: 'bubble',
        data: data,
        options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Chart.js Bubble Chart'
              }
            }
          },
      })

}

function ChartPie(mydata, chartid) {
    var terms = d3.group(mydata, d => d['glove']);
    terms_data = []
    terms_labels = []
    terms_colors = []

    var keyValues = []
    for (key of terms.keys()) {
      keyValues.push([ key, terms.get(key).length ])
    }
    keyValues.sort(function compare(kv1, kv2) {
      return kv1[0].localeCompare(kv2[0])
    })

    for (val of keyValues) {
      terms_labels.push(val[0]);
      terms_data.push(val[1]);
    }

    var myColor = d3.scaleOrdinal().domain(terms_labels)
    .range(d3.schemeSet2)
    for (val of keyValues) {
      terms_colors.push(myColor(val[0]))
    }
    var chart = new Chart(chartid, {
        type: 'doughnut',
        options: {
        elements: {
            center: {
                text: 'glove',
                color: '#FF6384', // Default is #000000
                fontStyle: 'Arial', // Default is Arial
                sidePadding: 20, // Default is 20 (as a percentage)
                minFontSize: 25, // Default is 20 (in px), set to false and text will not wrap.
                lineHeight: 25 // Default is 25 (in px), used for when text wraps
            }
        },
          maintainAspectRatio: true,
          responsive: true,
          legend: {
            display: true
          },
          plugins: {
            datalabels: {
                backgroundColor: function(context) {
                    return context.dataset.backgroundColor;
                  },
                  borderColor: 'white',
                  borderRadius: 50,
                  borderWidth: 5,
                  color: 'white',
                  anchor:'end',
            },
        },
        },
        data: {
          labels: terms_labels,
          datasets: [
            {
              data: terms_data,
              backgroundColor: terms_colors
            }
          ],
        }
      })
    }

function ChartBar(mydata, chartid) {
    var terms = d3.group(mydata, d => d['glove']);
    terms_data = []
    terms_labels = []
    terms_colors = []

    var keyValues = []
    for (key of terms.keys()) {
      keyValues.push([ key, terms.get(key).length ])
    }
    keyValues.sort(function compare(kv1, kv2) {
      return kv1[0].localeCompare(kv2[0])
    })

    for (val of keyValues) {
      terms_labels.push(val[0]);
      terms_data.push(val[1]);
    }

    var myColor = d3.scaleOrdinal().domain(terms_labels)
    .range(d3.schemeSet2)
    for (val of keyValues) {
      terms_colors.push(myColor(val[0]))
    }
    var chart = new Chart(chartid, {
        type: 'bar',
        options: {
            maintainAspectRatio: true,
            responsive: true,
            legend: {
            display: false
            },
            plugins: {
            datalabels: {
                formatter: (value, ctx) => {
                    let sum = 0;
                    let dataArr = ctx.chart.data.datasets[0].data;
                    dataArr.map(data => {
                        sum += data;
                    });
                    let percentage = (value*100 / sum).toFixed(2)+"%";
                    return percentage;
                },
                backgroundColor: function(context) {
                    return context.dataset.backgroundColor;
                    },
                    borderColor: 'white',
                    borderRadius: 50,
                    borderWidth: 5,
                    color: 'white',
                    anchor:'end',
            },
        },
          scales: {
            xAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: 'glove',
                  fontSize: 16
                }
              }
            ]
          }
        },
        data: {
            labels: terms_labels,
            datasets: [
            {
                data: terms_data,
                backgroundColor: terms_colors
            }
            ],
        }
        })
    }
