document.addEventListener("DOMContentLoaded", function () {
    const jsonForm = document.getElementById("jsonForm");
    const copyButton = document.getElementById("copy-button");

    let clickNum = 0;


    // Handle EQ Type selection
    const trackTypeSelect = document.querySelector("#track-mode");
    const panParamContainerMono = document.querySelector(".pan-parameter-container-mono");
    const panRightContainerStereo = document.querySelector("#pan-right-container");
    const panLeftContainerStereo = document.querySelector("#pan-left-container");
    trackTypeSelect.addEventListener("change", function () {
        if (trackTypeSelect.value === "STEREO") {
            panParamContainerMono.style.display = "none";
            panRightContainerStereo.style.display = "block";
            panLeftContainerStereo.style.display = "block";
        } else {
            panParamContainerMono.style.display = "block";
            panRightContainerStereo.style.display = "none";
            panLeftContainerStereo.style.display = "none";
        }
    });

    copyButton.addEventListener("click", function () {
        console.log("testing here");
        const formData = new FormData(jsonForm);
        let trackPan = [];
        let reverbPanValue = [];

        if (document.querySelector("#track-mode").value == "MONO") {
            trackPan.push(parseInt(formData.get('pan')));
            reverbPanValue.push(parseInt(formData.get('reverb-pan')));
        }
        else {
            trackPan.push(parseInt(formData.get('pan-left')));
            trackPan.push(parseInt(formData.get('pan-right')));
            reverbPanValue.push(parseInt(formData.get('reverb-pan-left')));
            reverbPanValue.push(parseInt(formData.get('reverb-pan-right')));
        }

        const jsonObject = {
            "track-name": formData.get('track-name'),
            "track-type": formData.get('track-type'),
            "track-audio-path": formData.get('track-audio-path'),
            "channel-mode": formData.get('track-mode'),
            "parameters": {
                "gain": parseFloat(formData.get('track-gain')),
                "pan": trackPan
            }
        };

        // Handle EQ
        let eqTypes = formData.getAll('eq-type');
        let eqGains = formData.getAll('eq-gain');
        let eqFreqs = formData.getAll('eq-freq');
        let eqQs = formData.getAll('eq-q');
        let eqArray = [];
        let eqJSONArray = [];
        // let eqJSONString = "";

        for (let index in eqTypes) {
            eqArray.push([eqTypes[index], eqFreqs[index], eqQs[index], eqGains[index]]);
        }

        for (let eqElement of eqArray) {
            if (eqElement.length == 3) {
                let tempArray = `{ "type": "${eqElement[0]}", "value": { "freq": ${eqElement[1]}, "q": ${eqElement[2]}}}`;
                eqJSONArray.push(JSON.parse(tempArray));
            }
            else {
                let tempArray = `{ "type": "${eqElement[0]}", "value": { "freq": ${eqElement[1]}, "q": ${eqElement[2]}, "gain": ${eqElement[3]}}}`;
                eqJSONArray.push(JSON.parse(tempArray));
            }
        }

        if (eqTypes != "") {
            // eqJSONString = eqJSONString.substring(0, eqJSONString.length - 1)
            jsonObject.eq = eqJSONArray;

            console.log("EQ was added");
        }

        // Handle Reverb
        let reverbName = formData.get('reverb-name');
        let reverbType = formData.get('reverb-type');
        let reverbGain = formData.get('reverb-gain');
        let reverbJSONString = `[{ "name" : "${reverbName}", "type" : "${reverbType}", "gain" : ${reverbGain}, "pan" : [${reverbPanValue}]}]`;

        if (reverbName != "" && reverbType != "") {
            jsonObject.parameters.reverb = JSON.parse(reverbJSONString);
        }

        // Handle Compression
        let compressionName = formData.get('compression-name');
        let compressionAttack = formData.get('compression-attack');
        let compressionRelease = formData.get('compression-release');
        let compressionRatio = formData.get('compression-ratio');
        let compressionJSONString = `{ "name" : "${compressionName}", "attack" : ${compressionAttack}, "release" : ${compressionRelease}, "ratio" : "${compressionRatio}"}`;

        if (compressionName != "") {
            jsonObject.parameters.compression = JSON.parse(compressionJSONString);
        }

        console.log(jsonObject);

        // Add logic to convert jsonObject to JSON string
        let jsonString = JSON.stringify(jsonObject, null, 2);
        // jsonString = jsonString.slice(-1,1)
        // console.log(jsonString)

        // Copy JSON string to clipboard
        const textarea = document.createElement("textarea");
        textarea.value = jsonString;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand("copy");
        document.body.removeChild(textarea);

        alert("JSON copied to clipboard!");
        window.location.reload();
    });

    // Handle the "Add Other Compression Parameter" button
    const addCompressionParamButton = document.querySelector(".add-compression-param");
    const compressionParameters = document.querySelector(".compression-section");
    addCompressionParamButton.addEventListener("click", function () {
        event.preventDefault();
        const parameterTemplate = document.createElement("div");
        parameterTemplate.classList.add("form-group");

        const paramNameInput = document.createElement("input");
        paramNameInput.type = "text";
        paramNameInput.classList.add("compression-param-name");
        paramNameInput.name = "compression-param-name[]";
        paramNameInput.placeholder = "Parameter Name";

        const paramValueInput = document.createElement("input");
        paramValueInput.type = "text";
        paramValueInput.classList.add("compression-param-value");
        paramValueInput.name = "compression-param-value[]";
        paramValueInput.placeholder = "Parameter Value";

        const removeButton = document.createElement("button");
        removeButton.classList.add("remove-compression-param");
        removeButton.textContent = "Remove";
        removeButton.addEventListener("click", function () {
            compressionParameters.removeChild(parameterTemplate);
        });

        parameterTemplate.appendChild(paramNameInput);
        parameterTemplate.appendChild(paramValueInput);
        parameterTemplate.appendChild(removeButton);

        compressionParameters.appendChild(parameterTemplate);
    });

    // Handle the "Show Reverb" button
    const showReverbButton = document.getElementById("show-reverb");
    const reverbSection = document.querySelector(".reverb-section");
    showReverbButton.addEventListener("click", function () {
        event.preventDefault();
        reverbSection.style.display = "block";
        if (document.querySelector("#track-mode").value == "MONO") {
            document.querySelector("#reverb-pan-mono").style.display = "block";
        }
        else {
            document.querySelector("#reverb-pan-left").style.display = "block";
            document.querySelector("#reverb-pan-right").style.display = "block";
        }
    });

    // Handle the "Show Compression" button
    const showCompressionButton = document.getElementById("show-compression");
    const compressionSection = document.querySelector(".compression-section");
    showCompressionButton.addEventListener("click", function () {
        event.preventDefault();
        compressionSection.style.display = "block";
    });

    // Handle the "Show EQ" button
    const showEqButton = document.getElementById("show-eq");
    const eqSection = document.querySelector(".eq-section");
    showEqButton.addEventListener("click", function () {
        event.preventDefault();
        eqSection.style.display = "block";
    });


    // Handle the "Add EQ Parameter" button
    const eqButtonParam = document.querySelector(".eq-button-param");
    const eqItemsContainer = document.querySelector(".eq-items");

    eqButtonParam.addEventListener("click", function () {
        clickNum++;
        event.preventDefault();
        const eqItemTemplate = document.createElement("div");
        eqItemTemplate.classList.add("eq-item");

        const eqTypeSelect = document.createElement("select");
        eqTypeSelect.name = "eq-type";
        eqTypeSelect.innerHTML = `
            <option value=""></option>
            <option value="HP">High Pass</option>
            <option value="LP">Low Pass</option>
            <option value="NOTCH">Notch</option>
            <option value="HS">High Shelf</option>
            <option value="LS">Low Shelf</option>
        `;

        eqTypeSelect.addEventListener("change", function () {
            event.preventDefault();
            // if (eqTypeSelect.value == "HP" || eqTypeSelect.value == "LP") {
            //     console.log("NOTCH WAS SELECTED");
            //     document.querySelector(`#eq-gain-${clickNum}`).style.display = "inline";
            //     document.querySelector(`#eq-q-${clickNum}`).style.display = "inline";
            //     document.querySelector(`#eq-freq-${clickNum}`).style.display = "inline";
            // }
            // else {
            document.querySelector(`#eq-gain-${clickNum}`).style.display = "inline";
            document.querySelector(`#eq-q-${clickNum}`).style.display = "inline";
            document.querySelector(`#eq-freq-${clickNum}`).style.display = "inline";
            // }
            // See if you can add a function to an individual element?
        })

        const eqFrequencyInput = document.createElement("input");
        eqFrequencyInput.type = "number";
        eqFrequencyInput.name = "eq-freq";
        eqFrequencyInput.placeholder = "Frequency";
        eqFrequencyInput.id = `eq-freq-${clickNum}`

        const eqQInput = document.createElement("input");
        eqQInput.type = "number";
        eqQInput.name = "eq-q";
        eqQInput.placeholder = "Q";
        eqQInput.id = `eq-q-${clickNum}`

        // Only if the type is Notch
        const eqGainInput = document.createElement("input");
        eqGainInput.type = "number";
        eqGainInput.name = "eq-gain";
        eqGainInput.placeholder = "Gain";
        eqGainInput.id = `eq-gain-${clickNum}`

        const removeButton = document.createElement("button");
        removeButton.classList.add("remove-eq-item");
        removeButton.textContent = "Remove";
        removeButton.addEventListener("click", function () {
            eqItemsContainer.removeChild(eqItemTemplate);
        });

        eqItemTemplate.appendChild(eqTypeSelect);
        eqItemTemplate.appendChild(eqFrequencyInput);
        eqItemTemplate.appendChild(eqQInput);
        eqItemTemplate.appendChild(eqGainInput);
        eqItemTemplate.appendChild(removeButton);

        eqItemsContainer.appendChild(eqItemTemplate);

        document.querySelector(`#eq-gain-${clickNum}`).style.display = "none";
        document.querySelector(`#eq-q-${clickNum}`).style.display = "none";
        document.querySelector(`#eq-freq-${clickNum}`).style.display = "none";
    });

    // Execute a function when the user presses a key on the keyboard
    document.addEventListener("keydown", function (event) {
        // If the user presses the letter "A" on the keyboard
        if (event.ctrlKey && event.key === "r") {
            event.preventDefault();
            showReverbButton.click();
        }

        if (event.ctrlKey && event.key === "c") {
            event.preventDefault();
            showCompressionButton.click();
        }

        if (event.ctrlKey && event.key === "e") {
            event.preventDefault();
            showEqButton.click();
        }

        if (event.ctrlKey && event.key === "q") {
            event.preventDefault();
            eqButtonParam.click();
        }
    });

});