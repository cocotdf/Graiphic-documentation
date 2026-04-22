<h1>Get update weights by index</h1>

<h2>Description</h2>

<p>Gets the “update_weight?” parameter of the layer selected by the index given as input. If the boolean is “True”, the weights are updated during the backward.</p>

<p align="center"><img alt="get_update_weight_by_idx" src="/_assets/shared-images/cd/cd1dea9a2b6b-get_update_weight_by_idx.png" width="220"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Model.Png" src="/_assets/shared-images/21/21498ef0ddd0-input_model.png" width="42"/></td>
      <td valign="top"><strong>Model in : </strong>model architecture.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer</em>, </strong>layer index.</td>
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
      <td valign="top" width="70%"><p><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="32"/><strong>update_weight : <em>cluster</em></strong></p>

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
      <td width="64" valign="top"><img alt="output_boolean.png" src="/_assets/shared-images/f4/f4787639135e-output_boolean.png" width="42"/></td>
      <td valign="top"><strong>update_weight? : <em>boolean, </em></strong>weights updated if true.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="update_weight" src="/_assets/shared-images/f2/f2d5dcf5ec91-update_weight.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
