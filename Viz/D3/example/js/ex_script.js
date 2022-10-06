d3.csv("https://raw.githubusercontent.com/chumo/Data2Serve/master/transition_clusters.csv", d3.autoType)
  .then(function(data){
      var myData = data;
      var mySVG = d3.select('svg');
      var circles = mySVG.selectAll("circle").data(myData);

circles.join("circle")
        .attr("cx",function(d){return d['Xi'];})
        .attr("cy",function(d){return d['Yi'];})
        .attr('fill',function(d){return d['color'];})
        .attr("r",2)
        .transition().duration(1000)
            .style('background', 'yellow')
        .attr("cx",function(d){return d['Xf'];})
        .attr("cy",function(d){return d['Yf'];});;
   });