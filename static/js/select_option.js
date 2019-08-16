    var cities=new Array(13);//创建一个二维数组存放地市,区县
    cities[0]=new Array("岳麓区","开福区","芙蓉区","望城区","天心区","雨花区","长沙县","浏阳市","宁乡市");
    cities[1]=new Array("天元区","石峰区","荷塘区","芦淞区","渌口区","醴陵市","茶陵县","炎陵县","攸县");
    cities[2]=new Array("岳塘区","雨湖区","湘乡市","韶山市","湘潭县");
    cities[3]=new Array("雁峰区","蒸湘区","南岳区","珠晖区","石鼓区","耒阳市","常宁市","祁东县","衡阳县","衡东县","衡山县","衡南县");
    cities[4]=new Array("双清区","北塔区","大祥区","武冈市","邵东市","洞口县","邵阳县","新邵县","绥宁县","新宁县","隆回县","城步县");
    cities[5]=new Array("岳阳楼区","君山区","云溪区","临湘市","汨罗市","岳阳县","湘阴县","平江县","华容县");
    cities[6]=new Array("武陵区","鼎城区","津市市","汉寿县","石门县","临澧县","桃源县","安乡县","澧县");
    cities[7]=new Array("永定区","武陵源区","慈利县","桑植县");
    cities[8]=new Array("赫山区","资阳区","沅江市","桃江县","安化县","南县");
    cities[9]=new Array("北湖区","苏仙区","资兴市","安仁县","桂阳县","宜章县","汝城县","嘉禾县","临武县","桂东县","永兴县");
    cities[10]=new Array("冷水滩区","零陵区","道县","蓝山县","新田县","江永县","双牌县","祁阳县","宁远县","东安县","江华县");
    cities[11]=new Array("鹤城区","洪江市","会同县","沅陵县","辰溪县","溆浦县","中方县","新晃县","芷江县","通道县","麻阳县","靖州县");
    cities[12]=new Array("娄星区","冷水江市","涟源市","新化县","双峰县");
    cities[13]=new Array("吉首市","龙山县","古丈县","永顺县","凤凰县","保靖县","花垣县");

//设置点击事件
    function changeCity(val){
        //alert(val);
        var cityEle=document.getElementById("district_select");//获取第二个下拉列表对象
        cityEle.options.length=0;//清空第二个下拉列表的option内容
        //1.先遍历省份
        for(var i=0;i<cities.length;i++){
            //2.创建城市的文本节点
            if(val==i) {
               ////3.遍历用户选择的省份下的城市
                for (var j=0;j<cities[i].length;j++){
                    //alert(cities[i][j]);
                    //创建文本节点
                     var textNode=document.createTextNode(cities[i][j]);
                     //创建option元素节点
                    var opEle=document.createElement("option");
                    //添加元素到子节点
                    opEle.appendChild(textNode);
                    //将创建的option元素节点添加到第二个下拉列表中去
                     cityEle.appendChild(opEle);
                }
            }
        }
    }