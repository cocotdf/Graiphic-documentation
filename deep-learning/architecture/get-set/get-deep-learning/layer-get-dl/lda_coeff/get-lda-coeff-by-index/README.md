<h1>Get “lda_coeff” by index</h1>

<h2>Description</h2>

<p>Gets the loss derivative attenuation coefficient of layer selected by the index given as input.</p>

<p align="center"><img alt="get_lda_coef_by_idx" src="/_assets/shared-images/02/02ce455aa23e-get_lda_coef_by_idx.png" width="220"/></p>

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
      <td valign="top" width="70%"><p><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="32"/><strong>lda_coeff :</strong><em><strong>cluster</strong></em></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32 Out.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer</em>,</strong> index of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String Out.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em>,</strong> name of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Out Single.Png" src="/_assets/shared-images/95/95831a40e0b5-out-single.png" width="42"/></td>
      <td valign="top"><strong>lda_coeff : <em>float</em>,</strong> loss derivative attenuation coefficient value.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="lda_coeff" src="/_assets/shared-images/6d/6d549d3e9430-lda_coeff.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>

<h3>Using the “Get lda_coeff by index” function</h3>

<p align="center"><img alt="get_lda_coeff_by_index" src="assets/get_lda_coeff_by_index.png" width="220"/></p>

<p>1 – Define Graph</p>

<p>We define the graph with one input and two Dense layers named Dense1 and Dense2. We set the Dense1 layer with a “lda_coeff” equal to 2 and the Dense2 layer with a “lda_coeff” equal to 5.</p>

<p>2 – Get Function</p>

<p>We use the “Get lda_coeff by index” function to get the value of the parameter of layer at index 2.</p>
