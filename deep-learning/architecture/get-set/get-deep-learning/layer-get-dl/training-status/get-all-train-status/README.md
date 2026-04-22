<h1>Get all training status</h1>

<h2>Description</h2>

<p>Gets for all layers contained in the model the state of the boolean “training_status”. If the boolean is “True”, then a layer backward is performed.</p>

<p align="center"><img alt="get_all_train_status" src="/_assets/shared-images/2f/2f73e886aea9-get_all_train_status.png" width="220"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Model.Png" src="/_assets/shared-images/21/21498ef0ddd0-input_model.png" width="42"/></td>
      <td valign="top"><strong>Model in : </strong>model architecture.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Model.Png" src="/_assets/shared-images/3c/3c881c79a647-output_model.png" width="42"/></td>
      <td valign="top"><strong>Model out : </strong>model architecture.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster Array Out.Png" src="/_assets/shared-images/ce/ce79fc3283cc-cluster-array-out.png" width="32"/><strong>training_status_array : <em>array</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32 Out.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer</em>,</strong> index of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String Out.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em>,</strong> name of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="booleen.png" src="/_assets/shared-images/e9/e9f30799ffbd-booleen.png" width="42"/></td>
      <td valign="top"><strong>training_status : <em>boolean</em>,</strong> returns the training status.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="train_status_array" src="assets/train_status_array.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>

<h3>Using the “Get All Train Status” function</h3>

<p align="center"><img alt="get_all_train_status" src="/_assets/shared-images/2f/2f73e886aea9-get_all_train_status.png" width="220"/></p>

<p>1 – Define Graph</p>

<p>We define the graph with one input and two Dense layers named Dense1 and Dense2 parameterized in different ways.</p>

<p>2 – Get Function</p>

<p>We use the “Get All Train Status” function to get the value of the “training?” parameter for all layers of the model.</p>
