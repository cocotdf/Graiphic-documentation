<h1>Remove Particle</h1>

<h2>Description</h2>

<p>Eliminates or keeps particles resistant to a specified number of 3 x 3 erosions. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/b0/b0dd0bff1579-remove_particle.png" alt="Remove_Particle.Png" width="325" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Image_Src.Png" src="/_assets/shared-images/35/35918d98277f-input_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Src : <em>class, </em></strong>type accepted <strong>U8</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top">Connectivity 4/8 (8) :<em> boolean, </em>specifies the type of connectivity used by the algorithm for particle detection. The connectivity mode directly determines whether an adjacent pixel belongs to the same particle or a different particle.
<ul>
<li>
<ul>
<li>True : particle detection is performed in connectivity mode 8</li>
<li>False : particle detection is performed in connectivity mode</li>
</ul>
</li>
</ul></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Cluster_2.Png" src="/_assets/shared-images/ab/ab143124dd51-input_cluster_2.png" width="42"/></td>
      <td valign="top"><strong>Remove Particle Parameters :<em> cluster,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top"><strong>Number Of Erosions : <em>integer, </em></strong>specifies the number of 3 x 3 erosions to apply to the image.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top"><strong>Square/Hexa (Square) :<em> boolean, </em></strong>specifies whether to treat the pixel frame as square or hexagonal during the transformation.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Boolean.Png" src="/_assets/shared-images/1c/1cd07c2c1382-input_boolean.png" width="42"/></td>
      <td valign="top">Low Pass/High Pass (Low) :<em> boolean, </em>specifies whether the objects resistant to n erosions are discarded or kept.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="assets/remove_particle_param.png" alt="remove_particle_param" width="150" /></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Image_Src.Png" src="/_assets/shared-images/24/24dc58704218-output_image_src.png" width="42"/></td>
      <td valign="top"><strong>Image Dst :<em> class</em></strong></td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
