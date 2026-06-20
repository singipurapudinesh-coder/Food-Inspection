document.addEventListener(

"DOMContentLoaded",

function(){

    const chart =

    document.getElementById(

    "chart"

    );

    if(!chart){

        return;

    }

    const ctx =

    chart.getContext(

    "2d"

    );

    new Chart(

    ctx,

    {

    type:"doughnut",

    data:{

    labels:[

    "Healthy",

    "Unhealthy"

    ],

    datasets:[

    {

    data:[

    75,

    25

    ],

    backgroundColor:[

    "#27ae60",

    "#e74c3c"

    ]

    }

    ]

    },

    options:{

    responsive:true,

    animation:{

    duration:2000

    },

    plugins:{

    legend:{

    position:"bottom"

    }

    }

    }

    }

    );

});