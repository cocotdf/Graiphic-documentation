<h1>Substract</h1>

<h2>Description</h2>

<p>Computes the difference of the inputs. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p><strong>Warning : A new tensor is created for the output if you substract two arrays together.</strong></p>

<p align="center"><img src="/_assets/shared-images/49/49a2e336aa2f-substract.png" alt="Substract.Png" width="155" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Tensor.Png" src="/_assets/shared-images/77/775fe37288a0-input_acc_inference.png" width="42"/></td>
      <td valign="top"><strong>x : <em>class, </em></strong>n-dimensional tensor (can be a scalar).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Single.Png" src="/_assets/shared-images/fd/fd47ddc3550b-input_single.png" width="42"/></td>
      <td valign="top"><strong>y : <em>float,</em></strong> scalar (can be a tensor).</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Tensor.Png" src="/_assets/shared-images/7c/7cfbb5bb0789-output_tensor.png" width="42"/></td>
      <td valign="top"><strong>x – y : <em>class,</em></strong> the difference between x and y.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Accelerator library to run it).</p>

<h3>Substract tensor with a scalar</h3>

<p align="center"><img src="assets/substract_tensor_scalar.png" alt="substract_tensor_scalar" width="260" /></p>

<h3>Substract scalar with a tensor</h3>

<p align="center"><img src="assets/substract_scalar_tensor.png" alt="substract_scalar_tensor" width="260" /></p>

<h3>Substract a tensor to another tensor</h3>

<p align="center"><img src="assets/substract_tensor_tensor.png" alt="substract_tensor_tensor" width="260" /></p>
