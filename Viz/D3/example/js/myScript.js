var myData = [50,150,250,350,450];
var mySVG = d3.select('svg');
var circles = mySVG.selectAll("circle").data(myData);

circles.enter()
        .append("circle")
        .attr("cx",function(d){return d;})
        .attr("cy",50)
        .attr("r",50);

        