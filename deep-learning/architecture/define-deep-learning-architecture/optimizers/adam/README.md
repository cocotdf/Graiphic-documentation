<h1>Adam</h1>

<h2>Description</h2>

<p>Optimizer that implements the Adam algorithm. Adam optimization is a stochastic gradient descent method that is based on adaptive estimation of first-order and second-order moments. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img alt="define_adam.png" src="/_assets/shared-images/e7/e7b4089cd8b3-define_adam.png" width="239"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Model.Png" src="/_assets/shared-images/21/21498ef0ddd0-input_model.png" width="42"/></td>
      <td valign="top"><strong>Model in : </strong>model architecture.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="75%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Numeric Cluster.Png" src="/_assets/shared-images/10/103a7c4dd6b3-numeric-cluster.png" width="42"/></td>
      <td valign="top"><strong> Parameters : <em>cluster,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Single.Png" src="/_assets/shared-images/e2/e22146c46f27-single.png" width="42"/></td>
      <td valign="top"><strong>learning rate :</strong> <em><strong>float</strong></em>, the learning rate.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Single.Png" src="/_assets/shared-images/e2/e22146c46f27-single.png" width="42"/></td>
      <td valign="top"><strong>beta 1 :</strong> <em><strong>float</strong></em>, the exponential decay rate for the 1st moment estimates.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Single.Png" src="/_assets/shared-images/e2/e22146c46f27-single.png" width="42"/></td>
      <td valign="top"><strong>beta 2 :</strong> <em><strong>float</strong></em>, the exponential decay rate for the 2nd moment estimates.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Single.Png" src="/_assets/shared-images/e2/e22146c46f27-single.png" width="42"/></td>
      <td valign="top"><strong>weight_decay :</strong> <em><strong>float</strong></em>, if set, weight decay is applied.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Single.Png" src="/_assets/shared-images/e2/e22146c46f27-single.png" width="42"/></td>
      <td valign="top"><strong>epsilon :</strong> <em><strong>float</strong></em>, a small constant for numerical stability.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Enum.Png" src="/_assets/shared-images/9d/9d61ac752ae1-enum.png" width="42"/></td>
      <td valign="top"><strong>adam mode : <em>enum, </em></strong>compatibility mode. Selects between different implementations of Adam depending on the framework. Options : <code>Pytorch</code> or <code>HuggingFace</code>.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="25%"><p align="center"><img alt="param_adam" src="assets/param_adam.png" width="220"/></p></td>
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

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>

<p align="center"><img alt="optimizer_exemple" src="/_assets/shared-images/96/963d1cec2cf1-optimizer_exemple.png" width="220"/></p>
