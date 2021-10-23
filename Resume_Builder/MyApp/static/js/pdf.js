window.onload = function () {

    console.log("hello")
    document.getElementById("download")
        .addEventListener("click", () => {
            // console.log("hello2")

            const resume = this.document.getElementById("doc2");
            
            // console.log(resume);
            // console.log(window);
            var opt = {
                // margin: .5,
                hmargin:  -0.60, 
                vmargin:  20, 
                filename: 'myfile.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { dpi: 192, letterRendering: true },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().from(resume).set(opt).save();
        })
}